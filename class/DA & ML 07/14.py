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


    plt.subplot(1, 2, 1)
    plt.title("Image")
    plt.imshow(img, cmap="gray")

    # pre processing
    blur = cv.medianBlur(img, 5)
    dst = cv.equalizeHist(img)

    plt.subplot(1, 2, 2)
    plt.title("Equalized")
    plt.imshow(blur, cmap="gray")
    plt.show()
