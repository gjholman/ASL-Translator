import cv2
import sys
import os

videoCapture = cv2.VideoCapture(0)

path_to_data = os.path.join("~", "Desktop", "Data")

# Load tensoflow model

while True:
    ret, frame = videoCapture.read()

    cv2.imshow('Video', frame)

    # Repeatedly, record and save images to be predicted

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

videoCapture.release()
cv2.destroyAllWindows()
