# DETECT SPOON AND GET COORDINATE FOR ROBOT
# AUTHOR: THAI-BINH-DUONG [VIET-NAM]
# CONTACT: +84.327.085.425
# CREATED: 21 DEC 2021
# VERSION: V2.5
# -----------------------------

import cv2
import numpy as np
import imutils
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)
cap.set(3,600)
cap.set(4,800)


while True:
    _,frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([70,90,20])
    upper_blue = np.array([151,255,255])
    # mask = cv2.threshold(hsv, 140, 250, cv2.THRESH_BINARY_INV)
    mask = cv2.inRange(hsv,lower_blue,upper_blue, cv2.THRESH_BINARY)
    # mask = cv2.threshold(img, 140, 250, cv2.THRESH_BINARY_INV)


    cnts = cv2.findContours(mask, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cv2.imshow("mask", mask)
    i = 0
    for c in cnts:

        area = cv2.contourArea(c)
        if (area > 22000) & (area < 30000):
            i = i + 1
            cv2.drawContours(frame, [c], -1, (0,255,0), 3)
            M = cv2.moments(c)
            cx = int(M["m10"]/(M["m00"])+0.1)
            cy = int(M["m01"]/(M["m00"])+0.1)
            cv2.circle(frame, (cx,cy),7,(0,0,255), -1)
            cv2.putText(frame, "Spoon:", (cx+9, cy+5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,1))
            cv2.putText(frame, str(int(i)), (cx + 65, cy+5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 1))

            cv2.putText(frame,"X=",  (cx-22, cy-16),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),1)
            cv2.putText(frame,str(int(cx)), (cx+12, cy-16),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),1)

            cv2.putText(frame,"Y=", (cx-22, cy+23),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),1)
            cv2.putText(frame,str(int(cy)), (cx+12, cy+23),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),1)


            rect = cv2.minAreaRect(c)
            box = np.int0(cv2.boxPoints(rect))
            cv2.drawContours(frame, [box], 0, (255, 255, 255), 2)  # OR


            print("BVDT area is ....", frame)
            cv2.imshow("frame",frame)

    k = cv2.waitKey(10)
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
