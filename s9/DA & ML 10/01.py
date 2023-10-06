from matplotlib import pyplot as plt
from sklearn.datasets import load_digits
from sklearn.neighbors import KNeighborsClassifier

X, y = load_digits(return_X_y=True)
print(X.shape)

model = KNeighborsClassifier(n_neighbors=3)

model.fit(X, y)
predict = model.predict(X)

plt.subplot(1, 2, 1)
plt.scatter(X[:, 0], X[:, 1], c=y)

plt.subplot(1, 2, 2)
plt.scatter(X[:, 0], X[:, 1], c=predict)

print(model.score(X, y) * 100)
plt.show()
