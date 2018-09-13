import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(1)

cv2.namedWindow('image')
cv2.createTrackbar('Hl','image',0,255,nothing)
cv2.createTrackbar('Sl','image',0,255,nothing)
cv2.createTrackbar('Vl','image',0,255,nothing)

cv2.createTrackbar('Hu','image',0,255,nothing)
cv2.createTrackbar('Su','image',0,255,nothing)
cv2.createTrackbar('Vu','image',0,255,nothing)
while(1):

    # Take each frame
    _, frame = cap.read()

    #selecting filter
    hl = cv2.getTrackbarPos('Hl','image')
    sl = cv2.getTrackbarPos('Sl','image')
    vl = cv2.getTrackbarPos('Vl','image')

    hu = cv2.getTrackbarPos('Hu','image')
    su = cv2.getTrackbarPos('Su','image')
    vu = cv2.getTrackbarPos('Vu','image')


    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    #hsv(0, 100%, 100%) hsv(10, 28%, 59%)
    lower_blue = np.array([hl,sl,vl])
    upper_blue = np.array([hu,su,vu])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
