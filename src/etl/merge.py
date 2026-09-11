"""
KAPASITA
Merge Layer

Tujuan:
- Menggabungkan seluruh dataset
- Berdasarkan kolom provinsi
"""

import pandas as pd
from functools import reduce
from loguru import logger


class DatasetMerger:

    @staticmethod
    def find_province_column(df):

        candidates = [
            "provinsi",
            "nama_provinsi",
            "province"
        ]

        for col in candidates:

            if col in df.columns:
                return col

        return None

    @staticmethod
    def merge(datasets: dict):

        prepared = []

        for name, df in datasets.items():

            province_col = (
                DatasetMerger.find_province_column(df)
            )

            if province_col is None:

                logger.warning(
                    f"{name} skipped "
                    f"(no province column)"
                )

                continue

            if province_col != "provinsi":

                df = df.rename(
                    columns={
                        province_col: "provinsi"
                    }
                )

            prepared.append(df)

        if len(prepared) == 0:

            raise ValueError(
                "No dataset available to merge"
            )

        master = reduce(

            lambda left, right:

            pd.merge(
                left,
                right,
                on="provinsi",
                how="outer"
            ),

            prepared
        )

        logger.success(
            f"Master dataset shape: "
            f"{master.shape}"
        )

        return master