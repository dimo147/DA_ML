import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("face.jpg", 0)

print(img.shape)

kernel = np.ones((30,30)) / 900
result = cv.filter2D(img,-1, kernel)
print(result.shape)


plt.imshow(result,cmap="gray")
plt.show()