import pandas as pd
from app.analytics.scoring import add_score, WEIGHTS
def test_weights_sum():
    assert abs(sum(WEIGHTS.values()) - 1.0) < 1e-9
def test_range():
    d = pd.DataFrame({k:[0,100] for k in WEIGHTS})
    o = add_score(d)
    assert o["SR_ICSS"].between(0,100).all()
