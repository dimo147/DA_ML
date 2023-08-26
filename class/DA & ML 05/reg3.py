import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("BTC-USD.csv")

y = df["Open"]
X = np.arange(len(y))

x_train = X[:300]
y_train = y[:300]

x_test = X[300:]
y_test = y[300:]


# train
model = np.poly1d(np.polyfit (x_train,y_train,48))
plt.plot(x_train,y_train,label= "Train")
plt.plot(x_test,y_test,label= "Test")

h = model(x_test)
plt.plot(x_test, h, label="Predict")

plt.legend()
plt.show()