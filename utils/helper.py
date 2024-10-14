import numpy as np
import pandas as pd
import os
import glob

METADATA_COLS = [
    'study_accession',
    'subject_accession', 
    'data_accession',
    'age',
    'gender',
    'desease', 
    'origin',
    'METHOD', 
    'TYPE',
    'PLATFORM_DESCRIPTION',
    'PLATFORM_GEO_ID',
    ]

def load_mapping(file_path):
    ensembl_to_gene = {}
    gene_to_ensembl = {}
    
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) == 2: 
                ensembl_id, gene_name = parts
                ensembl_to_gene[ensembl_id] = gene_name
                gene_to_ensembl[gene_name] = ensembl_id
        
    return ensembl_to_gene, gene_to_ensembl



ENSEMBL_TO_GENE, GENE_TO_ENSEMBL = load_mapping('utils/ENSEMBLID_mapping.txt')

## Here we still got plenty of unmapped results. Maybe https://biit.cs.ut.ee/gprofiler/page/apis provides more 
def convert_gene_names_to_ensembl(gene_names):
    ensembl_ids = []

    for gene_name in gene_names:
        mapping = GENE_TO_ENSEMBL.get(gene_name, None) 
        # When there is no mapping found return to the casual gene name
        if mapping==None:
            mapping = gene_name
    
        ensembl_ids.append(mapping)
    
    successful_conversions = sum(1 for ensembl_id in ensembl_ids if ensembl_id.startswith("ENSG"))
    success_rate = (successful_conversions / len(gene_names)) * 100
    print(f"Success rate convertion to ENSAMBLE: {success_rate}")
    return ensembl_ids

def convert_gene_names_to_ensembl_mygene(gene_names):
    import mygene

    mg = mygene.MyGeneInfo()
    result = mg.querymany(gene_names, scopes='symbol', fields='ensembl.gene', species='human')
    
    ensembl_ids = []
    for item in result:
        ensembl_id = item.get('ensembl', {}).get('gene') if 'ensembl' in item else None
        ensembl_ids.append(ensembl_id)
    
    return ensembl_ids


# Function to clean the 'age' column
def clean_age(value):
    import random
    if isinstance(value, str) and 'age: ' in value:
        if 'age: ' in value:
            replaced = value.replace('age: ', '')
            if replaced == 'NA':
                return np.nan
            return float(replaced)
        else:
            print(f'Error: {value}')
            return np.nan
    # here the over 90 handle need to be set
    elif isinstance(value, str) and 'x' in value:
        print(f'Error: {value}')

        return np.nan
    elif isinstance(value, str) and '90+' in value:
        return float(random.randint(90, 99))
    
    return value


def reorder_columns_by_metadata_and_gene_counts(df, metadata_cols=METADATA_COLS, gene_prefix='ENSG', gene_columns=[]):
    if len(gene_columns) == 0:
        gene_columns = [col for col in df.columns if col.startswith(gene_prefix)]  
    # Split the DataFrame into metadata and gene counts
    df_meta_only = df[metadata_cols]
    df_counts = df[gene_columns]
    
    # Create a new column order: metadata columns first, then gene count columns
    new_column_order = list(df_meta_only.columns) + list(df_counts.columns)
    
    # Reorder the DataFrame
    reordered_df = df[new_column_order]
    
    return reordered_df

def get_negative_values(df):
    description = df.describe().T
    negative_mins = description[description['min'] < 0]
    return negative_mins

def assemble_single_featureCounts_outputs_to_df(folder_path, file_endings='*.txt'):
    file_list = glob.glob(os.path.join(folder_path, file_endings))

    if len(file_list) == 0:
        print('Error: Empty file list')
        return
    
    dfs = []
    for file in file_list:
        df = pd.read_csv(file, skiprows=[0], sep='\t') # row 0 is a commented out metadata
        df = df.iloc[:, [0, -1]]
        sample_name = file.split('/')[-1] # remove the path infront of the filename
        sample_name = '.'.join(sample_name.split('.')[1:-3]) # remove PPMI-Phase1-IR3 as thid inof is in filename later, and remove '.featureCounts.GencodeV29.txt' as this is redundant too
        df.columns = ['Geneid', sample_name]
        dfs.append(df)
    combined_df = pd.concat(dfs, axis=1)
    combined_df = combined_df.loc[:, ~combined_df.columns.duplicated()]
    return df

def keep_latest_ensamble_version(df, duplicates, start_col=11):
    cols = list(df.iloc[:,start_col:].columns)
    ensemble_names = [col.split('.')[0] for col in cols if '.' in col ]
    ensemble_versions = [col.split('.')[1] for col in cols if '.' in col ]
    remove_cols = []
    for dupl in duplicates:
        indexes = [index for index, value in enumerate(ensemble_names) if value == dupl]  
        highest = 0 

        for i in indexes:
            ## There are a couple of _PAR_Y columns in PPMI, and i could not figure out what that is (Pseudoautosomal Region on Y Chromosome)
            if '_' in ensemble_versions[i]:
                ensemble_versions[i] = 0
            if int(ensemble_versions[i]) > highest:
                highest = int(ensemble_versions[i])
        
        while highest > 0:
            remove_cols.append(dupl + '.' + str(highest))
            highest = highest - 1
    
    print(df.shape)
    df = df.drop(columns=remove_cols, errors='ignore') #As not all versions inbetween must exist
    print(df.shape)

    return df 


