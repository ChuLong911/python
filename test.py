#
#'http://192.168.1.29:8080/video'
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
    #rzf = cv2.resize(frame, (600, 500))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([140,50, 50])
    upper_blue = np.array([180,255, 255])
#giảm nhiễu
    cap_blur = cv2.GaussianBlur(hsv, (11, 5), 0)
    #_,mask = cv2.threshold(cap_blur, 160, 255, cv2.THRESH_BINARY_INV)

    #mask = cv2.threshold(hsv, 140, 250, cv2.THRESH_BINARY_INV)
    mask = cv2.inRange(cap_blur,lower_blue,upper_blue, cv2.THRESH_BINARY)
    # mask = cv2.threshold(img, 140, 250, cv2.THRESH_BINARY_INV)

    cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    cnts = imutils.grab_contours(cnts)

    cv2.imshow("mask", mask)
    i = 0
    #b = max(cnts, key=cv2.contourArea)#
    for c in cnts:
        area = cv2.contourArea(c)
        if (area > 1000):# & (area < 30000):
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
            box = np.intp(cv2.boxPoints(rect))
            cv2.drawContours(frame, [box], 0, (0, 0, 255), 2)  # OR
            #goc quay
            # Giả sử chúng ta có hai vector
            v1 = np.array([1, 0])
            v2 = np.array([0, 1])

            # Tính góc giữa hai vector sử dụng tích vô hướng và định lý cosin
            dot_product = np.dot(v1, v2)
            norm_v1 = np.linalg.norm(v1)
            norm_v2 = np.linalg.norm(v2)

            cos_theta = dot_product / (norm_v1 * norm_v2)
            theta = np.arccos(cos_theta)

            # Chuyển đổi từ radian sang độ
            angle_in_degrees = np.degrees(theta)

            print("Góc giữa v1 và v2 là:", angle_in_degrees, "độ")

            #print("area is ....", frame)

            cv2.imshow("frame",frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
