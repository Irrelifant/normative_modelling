import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import time
import os
import sys
from scipy.io import mmread
from utils.helper import get_negative_values, METADATA_COLS, reorder_columns_by_metadata_and_gene_counts, convert_gene_names_to_ensembl, clean_age
from utils.plotting import violinplot_overall, scatter_plot, manhattanplot
import requests


ena_url_filereport_ERP = "https://www.ebi.ac.uk/ena/portal/api/filereport?result=read_run&accession="
ena_url_query_end = "&format=json&fields=study_accession,secondary_study_accession,sample_accession,secondary_sample_accession,experiment_accession,run_accession,submission_accession,tax_id,scientific_name,instrument_platform,instrument_model,library_name,nominal_length,library_layout,library_strategy,library_source,library_selection,read_count,base_count,center_name,first_public,last_updated,experiment_title,study_title,study_alias,experiment_alias,run_alias,fastq_bytes,fastq_md5,fastq_ftp,fastq_aspera,fastq_galaxy,submitted_bytes,submitted_md5,submitted_ftp,submitted_aspera,submitted_galaxy,submitted_format,sra_bytes,sra_md5,sra_ftp,sra_aspera,sra_galaxy,sample_alias,broker_name,sample_title,nominal_sdev,first_created,bam_ftp,bam_bytes,bam_md5"
ena_tsv_download_query_end= '&fields=study_accession,sample_accession,experiment_accession,run_accession,tax_id,instrument_platform,instrument_model,library_strategy,base_count,center_name,experiment_title,fastq_ftp,submitted_ftp,sra_ftp,sample_title&format=tsv&download=true&limit=0'
ena_json_query_end= '&fields=study_accession,sample_accession,experiment_accession,run_accession,tax_id,instrument_platform,instrument_model,library_strategy,base_count,center_name,experiment_title,fastq_ftp,submitted_ftp,sra_ftp,sample_title&format=json&limit=0'


###### ENA handling
#TODO check if this is even needed. right now the endpoint does not work anyways
# maybe we can also just directly download the TSV and the downloading script (Download all button for fastq files... this then downloads a lot of data if we shall execute it)
# Source https://www.ebi.ac.uk/ena/browser/api/swagger-ui/index.html#/content-controller/getSummary 



def download_ena_tsv(ena_accession):
    response = requests.get(ena_url_filereport_ERP + ena_accession + ena_tsv_download_query_end)
    if response.status_code == 200:
        #TODO check if requires attributes are in
        
        file_path = os.path.join(ena_accession, f'{ena_accession}.tsv')
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"File downloaded and saved as '{file_path}'.")
    else:
        print(f"Failed to retrieve data: {response.status_code}")



### this is same as the tsv but in json format
def get_ena_download_links(ena_accession, download_method_key='fastq_ftp'):
    download_links = []

    response = requests.get(ena_url_filereport_ERP + ena_accession + ena_json_query_end)
    if response.status_code == 200:
        data = response.json()
        for sample in data:
            sample_ftp_links = sample[download_method_key].split(';')
            download_links = download_links + sample_ftp_links

    else:
        print(f"Failed to retrieve data: {response.status_code}")

    file_path = os.path.join(ena_accession, f'{ena_accession}_download_links.txt')
    with open(file_path, 'w') as f:
        for link in download_links:
            f.write(link + '\n')
    return download_links

#TODO delete?
def get_filereport(ena_accession):
    ena_accession_primary = []

    requests.get(ena_url_filereport_ERP + ena_accession + ena_url_filereport_ERP)
    if response.status_code == 200:
        data = response.json()
        # now as we have gotten to the overview: 
        # TODO here we could automate the download for every sample ID in the filereport (without limit should show it all)
        
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        
        
def ena_handling(ena_accession):
    os.makedirs('ENA' + ena_accession, exist_ok=True)
    print(f"Directory '{ena_accession}' created or already exists.")

    download_ena_tsv(ena_accession)
    #TODO check tsv for age or sex info ...
    
    
    # now we check if we find required metadata (age, sex, desease state, platform ... )
    # if found Download BAM if exist (this would save us a ton of work ... 
    # if no BAM download fastq .... then we need to invest time to get counts... 
    bam_ftp_links = get_ena_download_links(ena_accession, 'bam_ftp')
    if len(download_links) == 0:
        return
    
    fastq_ftp_links = get_ena_download_links(ena_accession, 'fastq_ftp')