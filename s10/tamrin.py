import cv2
import pickle
import numpy as np
from sklearn.svm import SVC
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

x, y = load_digits(return_X_y=True)
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, random_state=42)

x_train = np.array([np.ravel(x) for x in x_train])
x_test = np.array([np.ravel(x) for x in x_test])

model = SVC(C=100)
model.fit(x_train, y_train)
result=model.predict(x_test)

knn = KNeighborsClassifier(n_neighbors=6,weights='distance')
knn.fit(x_train, y_train)
result=knn.predict(x_test)

print("Score: ", model.score(x_test, y_test) * 100)

img = cv2.imread("4.png", 0)
img = np.ravel(img).reshape(1,-1)
print("Predict = " ,model.predict(img))
print("Predict = " ,knn.predict(img))

with open('model.dat', 'wb') as files:
    pickle.dump(model, files)