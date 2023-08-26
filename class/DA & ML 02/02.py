import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

y = np.array([195,190,188,165,192,200,202,197])

mean = y.mean()

# variance = np.sum(np.power(y - mean , 2)) / n

variance = np.var(y)
std = np.std(y)       # np.sqrt(np.mean(np.power(y - mean, 2)))

plt.plot(y, label="Open Price")

# plt.plot([0, len(y)], [mean, mean], "g--", label="aaaa")
plt.plot([0, len(y)], [mean, mean], color="green", linestyle="dashed", label="Mean")
plt.plot([0, len(y)], [mean+std, mean+std], "b--", label="Up")
plt.plot([0, len(y)], [mean-std, mean-std], "r--", label="Down")

plt.legend()

plt.show()
