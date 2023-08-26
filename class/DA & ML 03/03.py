import cv2 as cv

img = cv.imread("face.jpg")
#
blur3 = cv.blur(img, (3,3))
blur30 = cv.blur(img, (30,30))
# 
sh = cv.GaussianBlur(img,(3,3),1,1)
cv.medianBlur()
cv.bilateralFilter()
# sh = cv.medianBlur()

# vertical line detector
# horizontal line detector

cv.imshow("Img", img)
cv.imshow("Blur3", blur3)
cv.imshow("Blur30", blur30)
cv.waitKey(0)