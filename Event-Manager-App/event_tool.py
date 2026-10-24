from pathlib import Path

import pandas as pd

SOURCE_DIR = Path(__file__).parent / "source_files"
"""
function : 
"""

def file_read(file_format: str, file_name: str) -> pd.DataFrame | None:
    path = SOURCE_DIR / file_name
    if file_format.lower() == 'csv':
        return file_name,pd.read_csv(path)
    elif file_format.lower() == 'json':
        return file_name,pd.read_json(path)
    else:
        return print('file format which is provided is not valid')



json_file_name,json_df_1=file_read('json','client_requests.json')
# if json_file_name =='client_requests.json' :