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

print(X.shape)
print(y.shape)

df = pd.DataFrame(X)
df.columns = ["Open","Low","High","Close"]
