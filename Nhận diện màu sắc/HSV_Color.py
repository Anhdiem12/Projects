import cv2
import numpy as np
def empty(c) :
    pass
cap = cv2.VideoCapture(0)
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,340)

cv2.createTrackbar("Hue min","TrackBars",0,179,empty)
cv2.createTrackbar("Hue max","TrackBars",176,179,empty)
cv2.createTrackbar("Sat min","TrackBars",40,255,empty)
cv2.createTrackbar("Sat max","TrackBars",255,255,empty)
cv2.createTrackbar("Val min","TrackBars",64,255,empty)
cv2.createTrackbar("Val max","TrackBars",255,255,empty)
while True:
    _, frame = cap.read()
    x = cv2.GaussianBlur(frame,(1,1),0)
    imgHSV = cv2.cvtColor(x, cv2.COLOR_BGR2HSV)
    hmin = cv2.getTrackbarPos("Hue min", "TrackBars")
    hmax = cv2.getTrackbarPos("Hue max", "TrackBars")
    smin = cv2.getTrackbarPos("Sat min", "TrackBars")
    smax = cv2.getTrackbarPos("Sat max", "TrackBars")
    vmin = cv2.getTrackbarPos("Val min", "TrackBars")
    vmax = cv2.getTrackbarPos("Val max", "TrackBars")
    print(hmin,hmax,smin,smax,vmin,vmax)

    lower = np.array([hmin, smin, vmin])
    upper= np.array([hmax,smax,vmax])
    mask= cv2.inRange(imgHSV,lower,upper)

    cv2.imshow("Original image",frame)
    cv2.imshow("Bo loc ",mask)
    cv2.waitKey(0)
