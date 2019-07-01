import cv2
import sys

videoCapture = cv2.VideoCapture(0)

while True:
    ret, frame = videoCapture.read()
    grayScale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurImage = cv2.GaussianBlur(grayScale, (5,5), 0)
    cannyImage = cv2.Canny(blurImage, 20, 150)

    cv2.imshow('Video', cannyImage)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

videoCapture.release()
cv2.destroyAllWindows()
