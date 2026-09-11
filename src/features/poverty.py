"""
KAPASITA

Poverty Feature Engine
"""

import pandas as pd
from sklearn.preprocessing import MinMaxScaler


class PovertyFeature:

    @staticmethod
    def generate(df, poverty_column):

        scaler = MinMaxScaler()

        values = df[[poverty_column]]

        df["poverty_risk"] = scaler.fit_transform(
            values
        )

        return df