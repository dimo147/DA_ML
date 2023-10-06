import pickle

import cv2
import numpy as np

file = open("model.dat", "rb")
model = pickle.load(file)


img = cv2.imread("1.png", 0)
img = np.ravel(img).reshape(1,-1)

print(model.predict(img))