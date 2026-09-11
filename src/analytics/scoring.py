"""
Priority Score Engine
"""


class PriorityScoring:

    @staticmethod
    def calculate(df):

        df["priority_score"] = (

            (df["poverty_risk"] * 0.30)

            +

            (df["education_gap"] * 0.25)

            +

            (df["teacher_gap"] * 0.20)

            +

            (df["inclusion_need"] * 0.15)

            +

            (df["digital_gap"] * 0.10)

        ) * 100

        return df