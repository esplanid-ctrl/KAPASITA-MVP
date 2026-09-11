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
from etl.extract import DataExtractor
from etl.transform import DataTransformer
from etl.merge import DatasetMerger
from etl.validate import DataValidatorimport pandas as pd
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
     
    def extract(self):

    	extractor = DataExtractor(
             self.raw_dir
        )

        self.datasets = extractor.extract_all()

    def validate(self):

        validated = {}

        for name, df in self.datasets.items():

            report = DataValidator.validate(df)

            print(name, report)

            df = DataValidator.remove_duplicates(df)

            df = DataValidator.fill_missing_numeric(df)

            df = DataValidator.fill_missing_text(df)

            validated[name] = df

    self.datasets = validated

    def transform(self):

        transformed = {}

        for name, df in self.datasets.items():

            transformed[name] = (
                DataTransformer.transform(df)
            )

    self.datasets = transformed

    def merge(self):

        self.master_dataset = (
            DatasetMerger.merge(
                self.datasets
            )
    )

    self.master_dataset.to_csv(
        "data/mart/master_dataset.csv",
        index=False
    )