print("Load Libraries ... ",end="")
import cv2
import numpy as np
from sklearn.svm import SVC
print("Done")

print("Load Dataset ... ",end="")
data = np.load("mnist.npz")
x_train = data['x_train']
y_train =data['y_train']
x_test = data['x_test']
y_test = data['y_test']
print("Done")

print("Normalize Dataset ... ", end="")
x_train = np.array([np.ravel(x) for x in x_train])
x_test = np.array([np.ravel(x) for x in x_test])
print("Done")


print("Train Model ... ", end="")
model = SVC()
model.fit(x_train, y_train)
print("Done")

print("Score ...")
print("Done")
print(model.score(x_test, y_test) * 100)


print("Predict ... ",end="")
img = cv2.imread("1.png", 0)
img = np.ravel(img).reshape(1,-1)
print("Done")

print("Predict = " ,model.predict(img))


import pickle
file = open("model.dat","wb")
pickle.dump(model, file)
file.close()

