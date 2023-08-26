import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

rmse_metric = []
learning_rate = 0.0001

df = pd.read_csv("BTC-USD.csv")

y = df["Open"]
X = np.arange(len(y))

n = len(X)

# 1
m = 1
b = y.mean()

h = m * X + b
print(f"h = {m} * X + {b}")

rmse = np.sqrt(np.mean(np.power(y - h ,2)))
print(rmse)

# 2
# sgd - m,b updated
for i in range(100):
    new_m = -(2/n) * np.sum(X * (y-h))
    new_b = -(2/n) * np.sum(y-h)

    m = m - (learning_rate * new_m)
    b = b - (learning_rate * new_b)

    # print(f"h = {m} * X + {b}")
    h = m * X + b
    rmse = np.sqrt(np.mean(np.power(y - h ,2)))
    print(rmse)

# 3
# sgd - m,b updated
# new_m = -(2/n) * np.sum(X * (y-h))
# new_b = -(2/n) * np.sum(y-h)
#
# m = m - (learning_rate * new_m)
# b = b - (learning_rate * new_b)
#
# print(f"h = {m} * X + {b}")
# h = m * X + b
# rmse = np.sqrt(np.mean(np.power(y - h ,2)))
# print(rmse)