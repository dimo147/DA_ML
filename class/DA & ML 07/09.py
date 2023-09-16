import numpy as np
from matplotlib import pyplot as plt


def sigmoid(x):
    return 1 / (1 + np.power(np.e, -x))



X = np.arange(-1000,1001)

plt.plot(sigmoid(X))
plt.show()