import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("SHAPES.jpg", 0)

print(img.shape)

kernel = np.array([[1,-1],
                   [-1,-1]])
result = cv.filter2D(img,-1, kernel)
print(result.shape)


plt.imshow(result)
plt.show()