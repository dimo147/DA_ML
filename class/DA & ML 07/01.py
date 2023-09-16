import numpy as np

X = np.arange(1, 11)
y = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]



x_train = X[:8]
y_train = y[:8]

x_test = X[8:]
y_test = y[8:]

print(x_train, y_train)
print(x_test, y_test)



