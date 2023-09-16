import os
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

path = os.getcwd() + "/dataset/"
file_list = []

for file in os.listdir(path):
    file_list.append(path + file)

for file in file_list:
    img = cv.imread(file, 0)

    # PreProcessing
    blur = cv.blur(img,(11,11))

    vector = np.ravel(blur)
    X = np.arange(len(vector))
    print(img.shape, vector.shape)



    model = np.poly1d(np.polyfit(
        x=X,
        y=vector,
        deg=5
    ))

    std = vector.std()
    regression = model(X)
    up = regression + std * 2.7
    down = regression - std * 2.3

    r = np.zeros_like(regression)
    r[vector > up] = 255
    r[vector < down] = 255

    r = r.reshape(img.shape)
    g = np.zeros_like(r)
    b = np.zeros_like(r)

    errors = cv.merge((r,g,b))

    plt.subplot(1, 3, 1)
    plt.plot(vector, label="Data")
    plt.plot(regression, label="Regression")
    plt.plot(up, "b--", label="Up")
    plt.plot(down, "b--", label="Down")

    plt.subplot(1, 3, 2)
    plt.title("Image")
    plt.imshow(img, cmap="gray")

    plt.subplot(1, 3, 3)
    plt.title("Errors")
    plt.imshow(errors, cmap="gray")
    plt.show()
