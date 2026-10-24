from pathlib import Path

import pandas as pd

SOURCE_DIR = Path(__file__).parent / "source_files"


def file_read(file_format: str, file_name: str) -> pd.DataFrame | None:
    path = SOURCE_DIR / file_name
    if file_format.lower() == 'csv':
        return pd.read_csv(path)
    elif file_format.lower() == 'json':
        return pd.read_json(path)
    else:
        return print('file format which is provided is not valid')


y = file_read('csv', 'bookings.csv')

print(y.head())
