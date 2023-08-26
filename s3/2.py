import numpy as np
import cv2

Img = np.zeros((512, 512, 3), dtype='uint8')

image = cv2.rectangle(Img, (356,256), (156, 456), (255, 250, 0), 1)

kernel = np.array([0,1,1,0])

result = cv2.filter2D(image, -1, kernel)

cv2.imshow('square', result)
cv2.waitKey(0)
cv2.destroyAllWindows()