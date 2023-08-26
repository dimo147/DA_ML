import cv2 as cv
import numpy as np

img = cv.imread("face.jpg", 0).astype(np.uint64)

noise_factor = 0.1

x = np.random.randint(0,int(255 * noise_factor), img.shape)

img = img + x

img = np.clip(x, 0,255)

print(img.min())
print(img.max())

img = img.astype(np.uint8)
print(img.dtype)

cv.imshow("Image",img)
cv.waitKey(0)