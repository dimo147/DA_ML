import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression

x, y = load_diabetes(return_X_y=True, as_frame=True)
x.drop(columns=["sex", "s4"], inplace=True)

model = LinearRegression()
features = x.columns

model.fit(x, y)
total_score = model.score(x,y) * 100

for i in range(len(features)):
    plt.subplot(1, len(features), i+1)
    plt.scatter(np.arange(len(x[features[i]].values)), x[features[i]])
    plt.title(features[i])

# plt.show()

scores = {}
print("Total Score: ",total_score)

for feature in features:
    model.fit(x[feature].values.reshape(-1, 1), y)
    score = model.score(x[feature].values.reshape(-1, 1),y) * 100
    print(f"{x[feature].name}:", score)
    scores[x[feature].name] = score
