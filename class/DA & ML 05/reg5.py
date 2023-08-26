import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("BTC-USD.csv")

y = df["Open"]
X = np.arange(len(y))

plt.plot(X,y,label= "Data")


diff = np.diff(y)

# plt.plot(X[1:],diff,label= "Difference")

upper = np.where(diff > 0)[0]
lower = np.where(diff < 0)[0]

plt.plot(X[upper],diff[upper],"g--", label="upper")
plt.plot(X[lower],diff[lower],"r--", label="lower")

plt.show()