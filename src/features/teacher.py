"""
Teacher Gap
"""

import pandas as pd


class TeacherFeature:

    @staticmethod
    def generate(df, teacher_index_column):

        df["teacher_gap"] = (
            100 -
            df[teacher_index_column]
        ) / 100

        return df