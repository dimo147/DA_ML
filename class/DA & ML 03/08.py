import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("face.jpg", 0)
print(img.dtype)
print(img.shape)

kernel = np.array(
    [[-1, -1, -1],
     [-1, 9, -1],
     [-1, -1, -1]]
)

kernel = kernel / kernel.sum()

result = cv.filter2D(img, -1, kernel)
print(result.shape)

plt.subplot(1, 3, 1)
plt.imshow(img, cmap="gray")

plt.subplot(1, 3, 2)
plt.imshow(result, cmap="gray")

kernel = np.ones((3, 3))
kernel = kernel / kernel.sum()

result = cv.filter2D(img, -1, kernel)

plt.subplot(1, 3, 3)
plt.imshow(result, cmap="gray")

plt.show()


