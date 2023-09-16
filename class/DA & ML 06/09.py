import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Data Extraction
from matplotlib import pyplot as plt
from scipy.signal import find_peaks

# Data Manipulation

df = pd.read_csv("EURUSD.csv", index_col="Date")
df.drop(columns=["Adj Close", "Volume"], inplace=True)

X = df.values
y = np.vstack((X[1:], np.zeros_like(X[0])))

model = LinearRegression()

model.fit(X, y)

print(model.score(X, y))

predict = model.predict(X)

plt.plot(y[:, 0])
plt.plot(predict[:, 0])

columns = ["Open", "Low", "High", "Close"]

for i in range(len(columns)):
    plt.subplot(2, 2, i + 1)
    plt.title(columns[i])
    plt.plot(y[:, i], label=columns[i])

    # Post Processing
    std = np.std(predict)
    up = y[:, i] + std
    down = y[:, i] - std
    plt.plot(up, "r--", label="Up")
    plt.plot(down, "r--", label="Down")

    p = predict[:, i]
    p[(p > up) | (p < down)] = 1
    plt.plot(p, "g--", label=f"{columns[i]} Predict")

    plt.legend()

plt.show()
