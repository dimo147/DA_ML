import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import load_diabetes

X, y = load_diabetes(return_X_y=True, as_frame=True)

# todo : train a model
# todo : which feature id the most important? whats second feature?    Why ?!

col = X.columns
n = len(col)

for i in range(n):
    plt.subplot(1, n + 1, i + 1)
    plt.scatter(np.arange(X.shape[0]), X[col[i]].values)
    plt.title(col[i])

plt.show()
