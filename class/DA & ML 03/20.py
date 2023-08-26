import cv2 as cv
import numpy as np

img = cv.imread("face.jpg")

# img[img<50] = 20
# img[(img>=50) & (img <100)] = 70
# img[(img>=100) & (img <150)] = 120
# img[(img>=150) & (img <200)] = 170
# img[(img>=200)] = 220

colors = 255 // 6

img = (img // colors) * colors

cv.imshow("Image", img)
cv.waitKey(0)
