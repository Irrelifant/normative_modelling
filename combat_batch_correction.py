#!/usr/bin/env python

import sys
import pandas as pd
from combat.pycombat import pycombat

def batch_correct_data(df, batch_column):
    # Define data columns
    df_reduced = df.loc[:, df.columns != batch_column]
    # Extract batch vector from DataFrame
    batch_vector = df[batch_column].values

    # Create an empty DataFrame to store the corrected data
    corrected_df = pd.DataFrame()

    # Iterate over each data column and perform batch correction using ComBat
        # Perform batch correction using ComBat
    corrected_data = pycombat(df_reduced.T, batch_vector)
        # Append corrected data to the DataFrame

    return corrected_df

def main():
    # Check if correct number of arguments is provided
    if len(sys.argv) != 4:
        print('ComBat batch correction. the input df needs to only contain the batch_vector and data (no metainfo)')
        print("Usage: python batch_correction.py <dataframe_csv_file> <batch_column> <output_name>")
        sys.exit(1)

    # Read DataFrame from CSV file
    dataframe_csv_file = sys.argv[1]
    batch_column = sys.argv[2]
    output_name = sys.argv[3]
    try:
        df = pd.read_csv(dataframe_csv_file)
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)

    # Perform batch correction
    corrected_df = batch_correct_data(df, batch_column)

    # Save corrected DataFrame to CSV
    corrected_df.to_csv(output_name, index=False)
    print("Batch correction completed. Corrected data saved to corrected_data.csv")

if __name__ == "__main__":
    main()
