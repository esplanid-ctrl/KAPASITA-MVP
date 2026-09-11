"""
KAPASITA
Data Profiling Agent

Tujuan:
- Membaca dataset
- Mendeteksi kolom
- Missing value
- Duplicate
- Data type
"""

from pathlib import Path
import pandas as pd
import json


class DatasetProfiler:

    def __init__(self, file_path):

        self.file_path = Path(file_path)

    def load_file(self):

        ext = self.file_path.suffix.lower()

        if ext == ".csv":

            return pd.read_csv(self.file_path)

        elif ext in [".xlsx", ".xls"]:

            return pd.read_excel(self.file_path)

        else:

            raise ValueError(
                f"Unsupported file: {ext}"