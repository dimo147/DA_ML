# pip install opencv-python
# pip install opencv-contrib-python

# Computer Vision

import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("face.jpg",0)
# BGR

print(type(img))
print(img.shape)

img[img>200] = 255
img[img<=200] = 0

# img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# img = cv.cvtColor(img, cv.COLOR_BGR2HSB)
plt.imshow(img,cmap="gray")
plt.show()

# cv.imshow("Img", img)
# cv.waitKey(0)