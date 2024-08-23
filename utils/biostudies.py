
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
from utils.ena import *

def filter_study_characteristics(study_json):
    requirements = ['Homo sapiens']
    useful_files = []
    is_useful = False
    
    # Navigate to the 'Source Characteristics' subsection in the json
    source_characteristics = find_type_section_by_string(study_json['section'], 'Source Characteristics')
    if source_characteristics:
        interesting_values = [item['value'] for item in source_characteristics]
        if "Homo sapiens" or 'human' in interesting_values and \
            any(["blood", "whole blood", "PBMC"]) in interesting_values:
            is_useful = True   
        ## TODO more filter attributes ?
            
    processed_data = find_type_section_by_string(study_json['section'], 'Processed Data')     
    if processed_data:       
        for files in processes_data.get('files', []):
            if is_useful_file(files.get('path')):
                useful_files.append(files.get('path'))
    
    
    return is_useful, useful_files


def get_biosample_query_response(biosample_url):
    response = requests.get(biosample_url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        return 0
        
def is_useful_file(filename):
    """
    Checks if a given filename is useful based on its contents and extension.

    Parameters:
    filename (str): The filename to be checked.

    Returns:
    bool: True if the filename is useful, False otherwise.
    """
    
    filename = filename.lower()
    
    # Check if "count" is in the filename or if it ends with .fastq or .fq
    if "count" in filename:
        return True
    
    if filename.endswith(".fastq") or filename.endswith(".fq"):
        return True

    return False

# Recursive function to find by 'type'
def find_type_section_by_string(section, search='Source Characteristics'):
    """
    Recursively searches for a section of a specific type within a given section.

    Args:
        section (dict): The section to search within.
        search (str): The type of section to search for. Defaults to 'Source Characteristics'.

    Returns:
        dict or None: The attributes of the found section, or None if not found.
    """
    
    # Check if the section is of type "search"
    if type(section) is not dict: 
        return
    
    if section.get("type") == search:
        return section.get("attributes")
    
    # If not, check subsections recursively
    if "subsections" in section:
        for subsection in section["subsections"]:
            result = find_type_section_by_string(subsection, search)
            if result:
                return result
    return None


def get_key_structure_for_string(section, search = 'links'):
    if isinstance(section, list):
        get_key_structure_for_string(section[0])
    
    if search in section:
        # Extract the structure of the first "links" entry
        return section[search]

    # If not, check subsections recursively
    if "subsections" in section:
        for subsection in section["subsections"]:
            result = get_key_structure_for_string(subsection, search)
            if result:
                return result
    return

def link_block_handling(found_link):
    is_ena = False
    
    if isinstance(found_link, list):
        found_link = found_link[0]
        
    if type(found_link) is not dict:
        return 
    
    if "url" in found_link:
        is_ena = found_link['url'].startswith('ERP')
        
    #NOTE ENA handling 
    if is_ena:
    
        ena_handling(found_link['url'])
        
    #TODO other link source handling here :)