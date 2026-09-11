"""
Digital Gap Feature
"""

import pandas as pd


class InternetFeature:

    @staticmethod
    def generate(df, internet_column):

        df["digital_gap"] = (
            100 -
            df[internet_column]
        ) / 100

        return df