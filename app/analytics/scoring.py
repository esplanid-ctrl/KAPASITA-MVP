import pandas as pd

WEIGHTS = {"INC":0.30, "CAP":0.25, "SOC":0.20, "DIG":0.15, "POL":0.10}

def percentile_need(series, bad_high=True):
    rank = series.rank(pct=True, method="average")
    return 100 * rank if bad_high else 100 * (1-rank)

def add_score(df):
    out = df.copy()
    for k in WEIGHTS:
        if k not in out:
            out[k] = 50.0
    out["SR_ICSS"] = sum(WEIGHTS[k]*out[k].fillna(50) for k in WEIGHTS).clip(0,100)
    out["confidence"] = out.get("confidence", pd.Series(50.0, index=out.index)).clip(0,100)
    return out
