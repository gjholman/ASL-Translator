import cv2
import sys
import os

videoCapture = cv2.VideoCapture(0)

path_to_data = os.path.join("~", "Desktop", "Data")

while True:
    ret, frame = videoCapture.read()

    cv2.imshow('Video', frame)

    # On keystroke, record a letter and save to the path_to_data directory

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

videoCapture.release()
cv2.destroyAllWindows()
