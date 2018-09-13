import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(1)

cv2.namedWindow('image')
cv2.createTrackbar('Hl1','image',0,180,nothing)
cv2.createTrackbar('Sl1','image',0,255,nothing)
cv2.createTrackbar('Vl1','image',0,255,nothing)

cv2.createTrackbar('Hu1','image',0,180,nothing)
cv2.createTrackbar('Su1','image',0,255,nothing)
cv2.createTrackbar('Vu1','image',0,255,nothing)

cv2.createTrackbar('Hl2','image',0,180,nothing)
cv2.createTrackbar('Sl2','image',0,255,nothing)
cv2.createTrackbar('Vl2','image',0,255,nothing)

cv2.createTrackbar('Hu2','image',0,180,nothing)
cv2.createTrackbar('Su2','image',0,255,nothing)
cv2.createTrackbar('Vu2','image',0,255,nothing)

while(1):

    # Take each frame
    _, frame = cap.read()

    #selecting filter
    hl1 = cv2.getTrackbarPos('Hl1','image')
    sl1 = cv2.getTrackbarPos('Sl1','image')
    vl1 = cv2.getTrackbarPos('Vl1','image')

    hl2 = cv2.getTrackbarPos('Hl2','image')
    sl2 = cv2.getTrackbarPos('Sl2','image')
    vl2 = cv2.getTrackbarPos('Vl2','image')

    hu1 = cv2.getTrackbarPos('Hu1','image')
    su1 = cv2.getTrackbarPos('Su1','image')
    vu1 = cv2.getTrackbarPos('Vu1','image')

    hu2 = cv2.getTrackbarPos('Hu2','image')
    su2 = cv2.getTrackbarPos('Su2','image')
    vu2 = cv2.getTrackbarPos('Vu2','image')

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    #hsv(0, 100%, 100%) hsv(10, 28%, 59%)
    lower_blue1 = np.array([hl1,sl1,vl1])
    upper_blue1 = np.array([hu1,su1,vu1])

    lower_blue2 = np.array([hl2,sl2,vl2])
    upper_blue2 = np.array([hu2,su2,vu2])

    # Threshold the HSV image to get only blue colors
    mask1 = cv2.inRange(hsv, lower_blue1, upper_blue1)
    mask2 = cv2.inRange(hsv, lower_blue2, upper_blue2)

    weightedSum = cv2.addWeighted(mask1,1.0,mask2,1.0,0.0)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask=weightedSum)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',weightedSum)
    cv2.imshow('res',res)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
