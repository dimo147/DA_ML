import cv2
import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import load_digits
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

X,y = load_digits(return_X_y=True)

x_train,x_test,y_train,y_test = train_test_split(X,y,train_size=0.8,random_state=20,stratify=y)

model = SVC(gamma=0.001)

model.fit(x_train, y_train)

predicted = model.predict(x_train)

print(model.score(x_test, y_test) * 100)

