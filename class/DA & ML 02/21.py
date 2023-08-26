import numpy as np
import pandas as pd


btc = pd.read_csv("BTC-USD.csv")

print(btc["Open"].shape)

print(np.array(btc["Open"]).reshape(6, -1))
print(btc["Open"].values.reshape(6, -1))

