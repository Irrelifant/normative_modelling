
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import seaborn as sns


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
    
    successful_conversions = sum(1 for ensembl_id in ensembl_ids if ensembl_id is not None)
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

def violinplot_overall(df, x_topic='GENDER', y_topic='MAX_SUBJECT_AGE_IN_YEARS', hue_split='GENDER', bin_name='test_bin'):
    sns.violinplot(x=x_topic, y=y_topic, hue=hue_split, data=df[[x_topic, y_topic]], split=True)
    try:
        os.makedirs(f'{bin_name}')
    except FileExistsError:
    # directory already exists
        pass

    if bin_name != 'test_bin':
        plt.show()
    else:
        plt.savefig(f'{bin_name}/violin_overall.png')
    
    
def manhattanplot(df, start_col=8, end_col=-1, save_name='default'):
    if end_col == -1: 
        markers = df.columns[start_col:]
    else:
        markers = df.columns[start_col:end_col]
    expression_values = [df[col].median() for col in markers] 

    try:
        os.makedirs(f'{save_name}')
    except FileExistsError:
    # directory already exists
        pass

    # Plot
    plt.figure(figsize=(10, 6))
    plt.scatter(markers, expression_values, s=10, color='blue', alpha=0.5)
    plt.xticks([])  # Remove x ticks
    plt.xlabel('Marker Name')
    plt.ylabel('Expression Value median')
    plt.title('median Gene Expression Dot Plot')
    plt.tight_layout()
    plt.savefig(f'{save_name}/manhattan_plot.png')
    plt.show()

def scatter_plot(df, x_ID='DUSP22', y_ID='age', hue_ID='study_accession'):
    plot = sns.jointplot(x=x_ID, y=y_ID, data=df, kind='scatter', hue=hue_ID)
    
    plot.ax_joint.legend_.remove()

    #plot.ax_joint.scatter(df[x_ID], df[y_ID], c=df['study_accession'])
    plt.xlabel(f'{x_ID}')
    plt.ylabel(f'{y_ID}')
   # plt.title(f'{x_ID} - {y_ID}')
    plt.show()