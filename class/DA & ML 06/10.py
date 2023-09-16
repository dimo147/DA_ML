# mnist 0...9 70000 * 28 * 28
# 1797 * 8 * 8
# classification
import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import load_digits

X,y = load_digits(return_X_y=True)

print(X)
print(y)

print(X.shape)
print(y.shape)

n = 1000
plt.imshow(X[n].reshape(8,8),cmap="gray")
plt.title(y[n])
plt.show()

print(np.unique(y))
print(len(np.unique(y)))

