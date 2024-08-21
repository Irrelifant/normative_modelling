import pandas as pd
from collections import defaultdict


def read_prefixes_from_metadata_txt(txt_path, prefix= '!Sample_', separator='\t'):
  # Reading...
  with open(txt_path, 'r') as file:
    lines = file.readlines()

  # I only want lines starting with !Sample_ 
  sample_lines = [line.strip() for line in lines if line.startswith(prefix)]

  # Parse the data
  headers = []
  data_dict = defaultdict(list)
  
  for line in sample_lines:
    parts = line.split(separator)
    header = parts[0]
    data = parts[1:]
    
    # If header already exists, append a suffix to make it unique
    count = 1
    new_header = header
    while new_header in headers:
      count += 1
      new_header = f"{header}.{count}"
    
    headers.append(new_header)
    data_dict[new_header] = data

  # Convert to DataFrame
  df = pd.DataFrame.from_dict(data_dict, orient='index').transpose()

  #Rename columns to remove the prefix
  new_columns = {col: col.replace(prefix, '') for col in df.columns}
  df.rename(columns=new_columns, inplace=True)

  # remove string artifacts (leading and ending "")
  df = df.applymap(lambda x: x.strip('"') if isinstance(x, str) else x)

  return df