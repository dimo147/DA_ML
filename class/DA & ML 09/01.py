import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import make_blobs


X,y = make_blobs(centers=2,cluster_std=5)

plt.scatter(X[:,0], X[:,1], c=y)

X1 = X[:,0]
X2 = X[:,1]

# X1, X2 = np.meshgrid(x1, x2)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
sigma2 = 1
R1 = np.exp(-(X1 ** 2 + X2 ** 2) / (2 * sigma2))
surf = ax.scatter(X1, X2, R1, cmap=plt.cm.coolwarm,c=y)
plt.title('$\sigma^2$ = {:.1f}'.format(sigma2))
plt.show()