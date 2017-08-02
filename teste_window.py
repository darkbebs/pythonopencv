import numpy as np
import cv2

def nothing(x):
    pass

#img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image')
cv2.createTrackbar('H','image',0,255,nothing)

while(1):
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    
    cv2.imshow('image')
    r = cv2.getTrackbarPos('R','image')
    print r

cv2.destroyAllWindows()