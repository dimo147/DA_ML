from matplotlib import pyplot as plt
from sklearn.datasets import make_regression


X,y = make_regression(n_samples=1000, n_features=1)

print(X.mean())
print(X.std())


print(y.mean())
print(y.std())


# plt.hist(y)
plt.plot(X,y)
plt.show()

print(X)
