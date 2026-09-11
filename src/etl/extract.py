"""
KAPASITA
Extract Layer

Tujuan:
- Load seluruh dataset mentah
- Support CSV dan Excel
- Menyimpan dataset dalam dictionary
"""

from pathlib import Path
import pandas as pd
from loguru import logger


SUPPORTED_FILES = [".csv", ".xlsx", ".xls"]


class DataExtractor:

    def __init__(self, raw_dir: str):

        self.raw_dir = Path(raw_dir)

    def load_file(self, file_path: Path):

        suffix = file_path.suffix.lower()

        logger.info(f"Loading {file_path.name}")

        if suffix == ".csv":

            return pd.read_csv(file_path)

        elif suffix in [".xlsx", ".xls"]:

            return pd.read_excel(
                file_path,
                sheet_name=0
            )

        raise ValueError(
            f"Unsupported extension: {suffix}"
        )

    def extract_all(self):

        datasets = {}

        for file in self.raw_dir.rglob("*"):

            if file.suffix.lower() not in SUPPORTED_FILES:
                continue

            try:

                df = self.load_file(file)

                datasets[file.stem] = df

                logger.success(
                    f"{file.name} loaded ({df.shape})"
                )

            except Exception as e:

                logger.error(
                    f"{file.name} failed: {e}"
                )

        return datasets