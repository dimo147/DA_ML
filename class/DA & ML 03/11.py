import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def on_trackbar(x):
    img = np.ones((500,500),dtype='un') * x
    cv.imshow("A", img)
    cv.waitKey(0)
    print(x)

img = np.zeros((500,500))

cv.imshow("Image", img)

cv.createTrackbar("Color", "Image" , 0, 255, on_trackbar)

cv.waitKey(0)
