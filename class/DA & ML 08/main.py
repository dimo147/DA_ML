import time

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import make_blobs
from sklearn.linear_model import LogisticRegression

model_report = []

samples = [5000, 10000, 20000, 30000, 100000, 200000, 500000]
features = [2, 3, 4, 5, 6, 7, 8, 9, 10]
std = np.arange(1, 5, 0.5)

for s in samples:
    for f in features:
        for st in std:
            print("Samples : {:<10} \t\t Features : {:<10} \t\t STD : {:<10}".format(s, f, st))
            t0 = time.time()
            X, y, centers = make_blobs(
                n_samples=s,
                n_features=f,
                cluster_std=st,
                return_centers=True,
                random_state=32
            )
            model = LogisticRegression()
            model.fit(X, y)
            t1 = time.time()
            model_report.append({"samples": s,
                                 "features": f,
                                 "std": st,
                                 "score": model.score(X, y) * 100,
                                 "time": round(t1 - t0, 6)})

# plt.subplot(2, 1, 1)
# plt.title("Sample/Score")
# plt.xlabel("Samples")
# plt.ylabel("Score")
# plt.plot(samples, scores)
#
# plt.subplot(2, 1, 2)
# plt.title("Sample/Time")
# plt.xlabel("Samples")
# plt.ylabel("Time")
# plt.plot(samples, times)
#
# plt.show()

df = pd.DataFrame(model_report)
df.to_csv("result.csv", index=None)
