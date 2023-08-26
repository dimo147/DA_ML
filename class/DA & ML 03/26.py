import cv2 as cv


face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv.CascadeClassifier("haarcascade_eye.xml")

print("Start Capturing")
capture = cv.VideoCapture(0)


print("Capture Started")
while True:
    ret, frame = capture.read()

    faces = face_cascade.detectMultiScale(frame ,1.3,3)
    eyes = eye_cascade.detectMultiScale(frame ,1.3,3)

    for x,y,w,h in faces:
        cv.rectangle(frame, (x,y), (x+w,y+h), (0,0,255),2)

    for x,y,w,h in eyes:
        cv.circle(frame, (x+int(w/2),y+int(h/2)), int(w+h)//2 , (0,0,255),2)

    cv.imshow("Live", frame)

    if cv.waitKey(1)==27 :
        break

capture.release()
cv.destroyAllWindows()
