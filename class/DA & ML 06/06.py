import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Data Extraction
from matplotlib import pyplot as plt
from scipy.signal import find_peaks

df = pd.read_csv("EURUSD.csv", index_col="Date")
df.drop(columns=["Adj Close", "Volume"], inplace=True)

X = df[["Open", "Low", "High"]].values
y = df["Close"].values

# Model
model = LinearRegression()

# Train
model.fit(X, y)

# Predict
predict = model.predict(X)

# Evaluate
# print(model.score(X, y))
print(mean_squared_error(y, predict, squared=False))  # rmse

plt.plot(y, label="Data")
plt.plot(predict, label="Predict")

plt.legend()
plt.show()
