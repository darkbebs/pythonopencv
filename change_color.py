import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow('frame')
cv2.createTrackbar('H','frame',0,255,nothing)
cv2.createTrackbar('S','frame',0,255,nothing)
cv2.createTrackbar('V','frame',157,255,nothing)

cv2.createTrackbar('H_up','frame',255,255,nothing)
cv2.createTrackbar('S_up','frame',117,255,nothing)
cv2.createTrackbar('V_up','frame',255,255,nothing)


while(1):
    # Take each frame
    _, frame = cap.read()
    h = cv2.getTrackbarPos('H','frame')
    s = cv2.getTrackbarPos('S','frame')
    v = cv2.getTrackbarPos('V','frame')

    hh = cv2.getTrackbarPos('H_up','frame')
    ss = cv2.getTrackbarPos('S_up','frame')
    vv = cv2.getTrackbarPos('V_up','frame')

    # Convert BGR to HSV
    #hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([-50,100,100])
    upper_blue = np.array([15,255,255])

    lower_color = np.array([h,s,v])
    upper_color = np.array([hh,ss,vv])

    # Threshold the HSV image to get only blue colors
    #mask = cv2.inRange(frame, lower_blue, upper_blue)
    mask2 = cv2.inRange(frame, lower_color, upper_color)

    # Bitwise-AND mask and original image
    #res = cv2.bitwise_and(frame,frame, mask= mask)

    #cv2.imshow('hsv', hsv)
    cv2.imshow('frame',frame)
    #cv2.imshow('mask',mask)
    cv2.imshow('mask2',mask2)
    #cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

    if k == 115:
        cv2.imwrite('imagem_salva.png',frame)

    #img = np.zeros((512,512,3), np.uint8)
    #img = cv2.rectangle(img,(384,0),(510,128),(0,0,255),3)
    #cv2.imshow('desenho', img)

cv2.destroyAllWindows()