import cv2 as cv

img = cv.imread("faces.jpg")


face_detector = cv.CascadeClassifier("haarcascade_eye.xml")


faces = face_detector.detectMultiScale(img, 1.1, 3)

print(faces)
print(len(faces))

for x,y,w,h in faces:
    cv.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 1)

cv.imshow("Faces", img)
cv.waitKey(0)