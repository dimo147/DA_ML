import cv2 as cv
# frame rate    FPS

# capture = cv.VideoCapture("d:/recorder/Rec 2023-08-10 0001.mp4")
capture = cv.VideoCapture(0)


while True:
    status, frame = capture.read()


    frame[frame>150] = 255
    frame[frame<=150] = 0

    cv.imshow("Live", frame)
    if cv.waitKey(1) == 27:
        break

cv.imwrite("SCREEN-SHOT.JPG",frame)

capture.release()
cv.destroyAllWindows()