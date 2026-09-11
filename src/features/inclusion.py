"""
Inclusion Need
"""

import pandas as pd
from sklearn.preprocessing import MinMaxScaler


class InclusionFeature:

    @staticmethod
    def generate(df, disability_column):

        scaler = MinMaxScaler()

        df["inclusion_need"] = (
            scaler.fit_transform(
                df[[disability_column]]
            )
        )

        return df