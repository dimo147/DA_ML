import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("BTC-USD.csv")

y = df["Open"]
X = np.arange(len(y))


rmse_list = []

degree = list(range(1,21))

for i in degree:
    model = np.poly1d(np.polyfit (X,y,i))
    h = model(X)
    rmse = np.sqrt(np.mean(np.power(y - h ,2)))
    rmse_list.append(rmse)


# plt.plot(degree,rmse_list)

X_new = np.arange(380)
model = np.poly1d(np.polyfit (X,y,15))
h = model(X_new)
plt.plot(X,y)
plt.plot(X_new,h)
plt.show()