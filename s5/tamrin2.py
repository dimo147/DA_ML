'''
group the parts with difference lower than 3000
wiich is the best parameter to predict close (open, low, high, volume)
week day with highest 
'''
import numpy as np
from matplotlib import pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
import pandas as pd
df = pd.read_csv("BTC-USD.csv")

X = df[["Low"]]
y = df["Close"]
days = np.arange(len(y))

model = LinearRegression()
model.fit(X, y)

print(model.score(X, y) * 100)

plt.plot(days, y, label="True Data(y)")

predict = model.predict(X)

plt.plot(days, predict, label="Predict Data(y')")

plt.legend()
plt.show()
