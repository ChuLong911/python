#
#'http://192.168.1.29:8080/video'
# -----------------------------

import cv2
import numpy as np
import imutils
import math
from matplotlib import pyplot as plt


cap = cv2.VideoCapture(0)

cap.set(3,600)
cap.set(4,800)

while True:
    _,frame = cap.read()
    #rzf = cv2.resize(frame, (600, 500))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    lower_blue = np.array([140,50, 50])
    upper_blue = np.array([180,255, 255])
#giảm nhiễu
    cap_blur = cv2.GaussianBlur(hsv, (11, 5), 0)
    #_,mask = cv2.threshold(cap_blur, 160, 255, cv2.THRESH_BINARY_INV)

    #mask = cv2.threshold(cap_blur, 140, 250, cv2.THRESH_BINARY)
    mask = cv2.inRange(cap_blur,lower_blue,upper_blue, cv2.THRESH_BINARY)
    # mask = cv2.threshold(img, 140, 250, cv2.THRESH_BINARY_INV)

    cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    cnts = imutils.grab_contours(cnts)

    cv2.imshow("mask", mask)
    i = 0
    #b = max(cnts, key=cv2.contourArea)#
    for c in cnts:
        area = cv2.contourArea(c)
        if (area > 1000):# & (area < 3000):
            i = i + 1

            cv2.drawContours(frame, [c], -1, (0,255,0), 2)

            M = cv2.moments(c)
            cx = int(M["m10"]/(M["m00"])+0.1)
            cy = int(M["m01"]/(M["m00"])+0.1)
            cv2.circle(frame, (cx,cy),3,(0,0,255), -1)
            cv2.putText(frame, "TAM:", (cx+9, cy+5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,1))
            cv2.putText(frame, str(int(i)), (cx + 50, cy+5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255))

            cv2.putText(frame,"X=",  (cx-22, cy-16),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),1)
            cv2.putText(frame,str(int(cx)), (cx+12, cy-16),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),1)

            cv2.putText(frame,"Y=", (cx-22, cy+23),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),1)
            cv2.putText(frame,str(int(cy)), (cx+12, cy+23),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),1)
#suavien.................
            #for esp in np.linspace(0.0001, 0.001, 10):Q
                #peri = cv2.arcLength(c, True)
                #approx = cv2.approxPolyDP(c, esp * peri, True)
                # draw the approximated contour on the image
                #output =frame.copy()
                #cv2.drawContours(output, [approx], -1, (0, 255, 0), 2)
                #text = "esp={:.4f},N={}".format(esp, len(approx))
                #cv2.putText(output, text, (cx - 40, cy-30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

                # show approximated
                #print("thong tin : {}".format(text))
                #cv2.imshow("xap xi", output)
#......................

            rect = cv2.minAreaRect(c)

            #goc quay
            #  fit elipse
            _, _, angle = cv2.fitEllipse(c)
            P1x = cx
            P1y = cy
            length = 50
            # calculate vector line at angle of bounding box
            P2x = int(P1x + length * math.cos(math.radians(angle)))
            P2y = int(P1y + length * math.sin(math.radians(angle)))
            # draw vector line
            cv2.line(frame, (cx, cy), (P2x, P2y), (255, 255, 255), 5)
            # output center of contour
            print(P1x, P2y, angle)

            cv2.putText(frame, "Angle=", (cx - 150, cy + 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (211, 41, 217))
            cv2.putText(frame, str(int(angle)), (cx - 90, cy + 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (211, 41, 217))

            box = np.intp(cv2.boxPoints(rect))
            cv2.drawContours(frame, [box], 0, (0, 0, 255), 2)  # OR
            # draw vecto 0 degree
            start = (cx, cy)
            end = (cx, cy - 60)
            color = (0, 0, 255)
            frame = cv2.line(frame, start, end, color, 1)
            # draw line pass throw center
            rows, cols = frame.shape[:2]
            [vx, vy, x, y] = cv2.fitLine(c, cv2.DIST_L2, 0, 0.01, 0.01)
            lefty = int((-x * vy / vx) + y)
            righty = int(((cols - x) * vy / vx) + y)
            cv2.line(frame, (cols, righty), (cx, cy), (0, 0, 255), 1)
            #cv2.line(img, (cols - 1, righty), (0, lefty), (0, 255, 0), 2)

            print("area is ....", frame)

            cv2.imshow("frame",frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
