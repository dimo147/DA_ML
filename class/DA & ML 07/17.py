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
    # blur = cv.blur(img,(11,11))

    vector = np.ravel(img)
    X = np.arange(len(vector))
    print(img.shape, vector.shape)



    model = np.poly1d(np.polyfit(
        x=X,
        y=vector,
        deg=15
    ))

    std = vector.std()
    regression = model(X)
    up = regression + std * 2
    down = regression - std * 2

    correct = vector.copy()

    for i in range(len(regression)):
        if correct[i] > up[i]:
            correct[i] = up[i]

        if correct[i] < down[i]:
            correct[i] = down[i]



    plt.subplot(2, 2, 1)
    plt.plot(vector, label="Data")
    plt.plot(regression, label="Regression")
    plt.plot(up, "b--", label="Up")
    plt.plot(down, "b--", label="Down")

    plt.subplot(2, 2, 2)
    plt.title("Image")
    plt.imshow(img, cmap="gray")

    plt.subplot(2, 2, 3)
    plt.plot(vector, label="Data")
    plt.plot(regression, label="Regression")
    plt.plot(correct, label="Correct")

    plt.subplot(2, 2, 4)
    correct = correct.reshape(img.shape)
    plt.title("Correct")
    plt.imshow(correct, cmap="gray")
    plt.show()
