import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error
from sklearn.metrics import classification_report


# def sigmoid(x):
def logistic(x):
    return 1 / (1 + np.power(np.e, -x))


X = np.array([1, 2, 4, 7, 10, 16, 19, 20, 22, 24]).reshape(-1, 1)
y = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

model = LinearRegression()
model.fit(X, y)

predict = model.predict(X)

# print("RMSE :", mean_squared_error(y, predict, squared=False))

predict = logistic(predict)
predict[predict < 0.6] = 0
predict[predict >= 0.6] = 1
# predict[9] = 0

print("Regression Score :", model.score(X, y) * 100)

print("Classification Score : ", np.sum(y == predict) / 10 * 100)
# print("Report :", classification_report(y, predict))

# print(y)
# print(predict)

plt.scatter(X, y)
plt.plot(X, predict)
plt.show()
