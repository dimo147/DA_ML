import pandas as pd

# Data Extraction
from matplotlib import pyplot as plt
from scipy.signal import find_peaks

df = pd.read_csv("EURUSD.csv", index_col="Date")

# Data Cleaning
df.drop(columns=["Adj Close", "Volume"], inplace=True)

X = df["Close"].values

x = []
x.append(X[0])

for i in range(1, len(X) - 1):
    x.append((X[i - 1] + X[i] * 8 + X[i + 1]) / 10)

plt.subplot(3, 1, 1)
index_peaks = find_peaks(X)[0]
plt.scatter(index_peaks, X[index_peaks])

plt.plot(X)
plt.plot([0, 266], [1, 1])

plt.subplot(3, 1, 2)
plt.plot(x)
plt.plot([0, 266], [1, 1])

for i in range(10):
    x_ = []
    x_.append(x[0])

    for i in range(1, len(x) - 1):
        x_.append((x[i - 1] + x[i] * 8 + x[i + 1]) / 10)

    x = x_

plt.subplot(3, 1, 3)
plt.plot(x_)
index_peaks = find_peaks(x_)[0]
plt.scatter(index_peaks, X[index_peaks])
plt.plot([0, 266], [1, 1])

plt.show()
