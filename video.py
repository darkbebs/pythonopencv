import numpy as np
import cv2
cap = cv2.VideoCapture(0)
cv2.createTrackbar('H','image',0,255,nothing)

while(True):

    # Captura Frame
    ret, frame = cap.read()

    cv2.rectangle(frame,(384,0),(510,128),(0,255,0),3)

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()