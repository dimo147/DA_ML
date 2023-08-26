# pip install scikit-learn
import numpy as np
from matplotlib import pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
import pandas as pd

df = pd.read_csv("BTC-USD.csv")

X = df["Open"].values.reshape(-1,1)
y = df["Close"]

m = len(y)
train_size = int(0.8 * m)

days = np.arange(m)

# train
model = LinearRegression(n_jobs=-1)
model.fit(X[:train_size], y.iloc[:train_size])

# test
# evaluate
print(model.score(X, y) * 100)

plt.plot(days, y, label="True Data(y)")
# predict

predict = model.predict(X[train_size:])

print(mean_squared_error(y.iloc[train_size:], predict))

plt.plot(days[train_size:], predict, label="Predict Data(y')")

plt.legend()
plt.show()

print(model.coef_)
print(model.intercept_)
