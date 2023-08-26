import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("BTC-USD.csv")

y = df["Open"]
X = np.arange(len(y))

# train
model = np.poly1d(np.polyfit (X, y,1))
plt.plot(X,y,label= "Data")

X = X[:200]
y = y.iloc[:200]

h = model(X)
plt.plot(X, h, label="Predict")

std = y.std()

plt.plot(X, h+std,"r--", label="Predict Up")
plt.plot(X, h-std,"r--", label="Predict Down")

plt.legend()
plt.show()