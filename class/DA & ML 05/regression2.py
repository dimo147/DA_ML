# pip install scikit-learn
import numpy as np
from matplotlib import pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
import pandas as pd

df = pd.read_csv("BTC-USD.csv")

X = df[["Low", "High", "Open"]]
y = df["Close"]
days = np.arange(len(y))

# train
model = LinearRegression()
model.fit(X, y)

# test
# evaluate
print(model.score(X, y) * 100)

plt.plot(days, y, label="True Data(y)")
# predict

predict = model.predict(X)

std = y.std()

print(mean_squared_error(y, predict))

plt.plot(days, predict, label="Predict Data(y')")

plt.plot(days, predict + std, "r--", label="Up")
plt.plot(days, predict - std, "r--", label="Down")

plt.legend()
plt.show()
