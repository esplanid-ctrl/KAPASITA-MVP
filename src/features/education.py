"""
Education Access Risk
"""

import pandas as pd


class EducationFeature:

    @staticmethod
    def generate(df, aps_column):

        df["education_gap"] = (
            100 - df[aps_column]
    