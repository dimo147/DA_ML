from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_blobs
import pandas as pd
import numpy as np
import time

samples = [500, 1000, 5000, 10000, 20000, 30000, 40000, 50000]
features = range(2,8)
std = [2, 2.4, 2.8, 3, 4, 5, 6, 7]

reports = []

for sample in samples:
    for feature in features:
        for st in std:
            t0 = time.time()
            x, y = make_blobs(
                n_samples=sample,
                n_features=feature,
                cluster_std=st,
                random_state=5,
            )
            model = LogisticRegression()
            model.fit(x,y)
            predict = model.predict(x)
            score = model.score(x, y)
            t1 = time.time()
            report = {
                "sample": sample,
                "features": feature,
                "std": st,
                "score": score,
                "time": round(t1-t0, 6),
            }
            reports.append(report)


df = pd.DataFrame(reports, index=None)
df.to_csv("report.csv")
