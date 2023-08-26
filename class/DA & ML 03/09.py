import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("face.jpg")
# BGR
# cv.line(img,(100,100),(200,300),(255,0,0),20)
# cv.rectangle(img, (100,100),(200,300),(0,0,255),cv.FILLED)
# cv.circle(img, (200,200),100,(0,0,255),2)
# cv.ellipse(img,(200,200),(100,200),80,100,180,(0,0,255),cv.FILLED)
# cv.putText(img,"SALAM",(100,100), cv.FONT_HERSHEY_TRIPLEX,2, (0,0,255),2)

cv.imshow("Image", img)
cv.waitKey(0)