
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import seaborn as sns


def read_prefixes_from_metadata_txt(txt_path, prefix= '!Sample_'):

    # Reading...
    with open(txt_path, 'r') as file:
        lines = file.readlines()

    # I only want lines starting with !Sample_ 
    sample_lines = [line.strip() for line in lines if line.startswith(prefix)]

    # Extract headers and data
    headers = [line.split('\t')[0] for line in sample_lines]
    data = [line.split('\t')[1:] for line in sample_lines]

    # Create a dictionary with headers as keys and data as values
    data_dict = {header: column for header, column in zip(headers, data)}

    # Convert to DataFrame
    df = pd.DataFrame.from_dict(data_dict, orient='index').transpose()

    #Rename columns to remove the prefix
    new_columns = {col: col.replace(prefix, '') for col in df.columns}
    df.rename(columns=new_columns, inplace=True)

    # remove string artifacts (leading and ending "")
    df = df.applymap(lambda x: x.strip('"') if isinstance(x, str) else x)

    return df