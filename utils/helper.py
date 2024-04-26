
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import seaborn as sns



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