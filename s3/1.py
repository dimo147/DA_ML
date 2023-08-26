import numpy as np
import cv2

Img = np.zeros((512, 512, 3), dtype='uint8')

triangle_cnt = np.array([(156, 256), (356, 256), (256, 156)])
image = cv2.drawContours(Img, [triangle_cnt], 0, (255, 250, 255), 8)

image = cv2.rectangle(image, (356,256), (156, 456), (255, 250, 255), 8)
image = cv2.rectangle(image, (226,365), (286, 456), (255, 250, 255), 8)

cv2.imshow('house', image)
cv2.waitKey(0)
cv2.destroyAllWindows()