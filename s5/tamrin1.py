import math
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("BTC-USD.csv")

y = df["Open"]
x = np.arange(len(y))

diff = np.diff(y)

abs = lambda t: math.fabs(t)
vfunc = np.vectorize(abs)
diff = vfunc(diff)
breaks = np.where(diff > 2000)[0]

plt.plot(x, y, color="r",  label="Main Data")

x = np.split(x, breaks)
parts = np.split(y, breaks)

for part, a in zip(parts, x):
    plt.plot(a, part)

plt.legend()
plt.grid()
plt.show()