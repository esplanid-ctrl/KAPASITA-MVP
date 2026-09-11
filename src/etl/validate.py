"""
KAPASITA
Validation Layer

Tujuan:
- Missing value check
- Duplicate check
- Numeric validation
"""

from loguru import logger
import pandas as pd


class DataValidator:

    @staticmethod
    def validate(df: pd.DataFrame):

        report = {}

        report["rows"] = len(df)

        report["columns"] = len(df.columns)

        report["missing"] = (
            df.isna()
            .sum()
            .to_dict()
        )

        report["duplicates"] = int(
            df.duplicated().sum()
        )

        return report

    @staticmethod
    def remove_duplicates(df):

        before = len(df)

        df = df.drop_duplicates()

        after = len(df)

        logger.info(
            f"Duplicates removed: {before-after}"
        )

        return df

    @staticmethod
    def fill_missing_numeric(df):

        numeric_cols = df.select_dtypes(
            include=["number"]
        ).columns

        for col in numeric_cols:

            median = df[col].median()

            df[col] = df[col].fillna(median)

        return df

    @staticmethod
    def fill_missing_text(df):

        text_cols = df.select_dtypes(
            include=["object"]
        ).columns

        for col in text_cols:

            df[col] = df[col].fillna("Unknown")

        return df