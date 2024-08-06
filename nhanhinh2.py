import cv2
import numpy as np

video = cv2.VideoCapture('http://192.168.1.29:8080/video')
while True:
    ret, frame = video.read()
    resize_fr = cv2.resize(frame, (600, 500))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    rs_fr = cv2.cvtColor(resize_fr, cv2.COLOR_BGR2GRAY)
    _,threshold = cv2.threshold(rs_fr, 160, 255, cv2.THRESH_BINARY)
    contours,_ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True )
        cv2.drawContours(resize_fr, [approx], 0, (0, 255, 0), 2)
        x = approx.ravel()[0]
        y = approx.ravel()[1]
        if len(approx) == 3:
            cv2.putText(resize_fr, "tam giac", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0))
        elif len(approx) == 4:
            cv2.putText(resize_fr, "hinh chu nhat", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0))
        elif len(approx) >5:
            cv2.putText(resize_fr, "hinh tron", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))

    cv2.imshow("webcam", resize_fr)
    cv2.imshow("den", threshold)
    if cv2.waitKey(1) & 0xFF == ord("q"):
     break
video.release()
cv2.destroyAllWindow()