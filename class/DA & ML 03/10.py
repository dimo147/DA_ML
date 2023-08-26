import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("face.jpg")
# BGR

r,g,b = cv.split(img)
zeros = np.zeros_like(r)

red = cv.merge((r,zeros,zeros))
green = cv.merge((zeros,g,zeros))
blue = cv.merge((zeros,zeros,b))

cv.imshow("Red", red )
cv.imshow("Green", green)
cv.imshow("Blue", blue)


cv.imshow("Image", img)
cv.waitKey(0)