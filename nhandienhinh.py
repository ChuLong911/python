import cv2
import numpy as np


#---------------------
def nothing(x):
    pass
video = cv2.VideoCapture(0)

cv2.namedWindow("adjustBar")

cv2.createTrackbar("L-H"," adjustBar",0,100, nothing)
cv2.createTrackbar("L-S"," adjustBar",66,255, nothing)
cv2.createTrackbar("L-V"," adjustBar",134,255, nothing)
cv2.createTrackbar("U-V"," adjustBar",243,255, nothing)
cv2.createTrackbar("U-S"," adjustBar",255,255, nothing)
#---------------------
while True:
    _,frame = video.read()
    resize_fr = cv2.resize(frame, (600, 500))
    hsv = cv2.cvtColor(resize_fr, cv2.COLOR_BGR2HSV)

    ls = cv2.getTrackbarPos("L-S", "adjustBar")
    lv = cv2.getTrackbarPos("L-V", "adjustBar")
    uh = cv2.getTrackbarPos("U-H", "adjustBar")
    us = cv2.getTrackbarPos("U-S", "adjustBar")
    uv = cv2.getTrackbarPos("U-V", "adjustBar")

    lower_red = np.array(lh, ls, lv)
    upper_red = np.array(uh, us, uv)

    mask = cv2.inRange(hsv, lower_red, upper_red)
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.erode(mask, kernel)

    contours,_ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        approx = cv2.approxPolyDP(cnt,0.02*cv2.arcLength(cnt, True), True )
        x = approx.ravel()[0]
        y = approx.ravel()[1]

        if area > 450:
            cv2.drawContours(resize_fr , [approx],0,(0,255,0),5)
            if len(approx)==3:
                cv2.putText(resize_fr, "tam giac", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0))
            elif len(approx) == 4:
                cv2.putText(resize_fr, "hinh chu nhat", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0))
            elif len(approx) > 5:
                cv2.putText(resize_fr, "hinh tron", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))
    cv2.imshow("mask", mask)
    cv2.imshow("webcam",resize_fr)

    if cv2.waitKey(0) &0xFF == ord("q"):
     break
video.release()
cv2.destroyAllWindow()
