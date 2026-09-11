"""
KAPASITA
Transform Layer

Tujuan:
- Standardisasi kolom
- Standardisasi provinsi
- Cleaning dataset
"""

import pandas as pd


PROVINCE_MAPPING = {
    "DKI JAKARTA": "DKI Jakarta",
    "DI YOGYAKARTA": "DI Yogyakarta",
    "PAPUA BARAT DAYA": "Papua Barat Daya",
}


class DataTransformer:

    @staticmethod
    def normalize_columns(df):

        df.columns = [

            col.strip()
               .lower()
               .replace(" ", "_")
               .replace("-", "_")

            for col in df.columns
        ]

        return df

    @staticmethod
    def normalize_province(df):

        province_candidates = [
            "provinsi",
            "nama_provinsi",
            "province"
        ]

        target_col = None

        for col in province_candidates:

            if col in df.columns:
                target_col = col
                break

        if target_col:

            df[target_col] = (
                df[target_col]
                .astype(str)
                .str.strip()
            )

            df[target_col] = (
                df[target_col]
                .replace(PROVINCE_MAPPING)
            )

        return df

    @staticmethod
    def remove_empty_rows(df):

        return df.dropna(how="all")

    @staticmethod
    def transform(df):

        df = DataTransformer.normalize_columns(df)

        df = DataTransformer.remove_empty_rows(df)

        df = DataTransformer.normalize_province(df)

        return df