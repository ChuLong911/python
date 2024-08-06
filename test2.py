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

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #cap_blur = cv2.GaussianBlur(gray, (11, 11), 0)

    mask = cv2.threshold(gray, 140, 250, cv2.THRESH_BINARY_INV)

    cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    #cnts = imutils.grab_contours(cnts)


    cv2.imshow("frame", frame)
    cv2.imshow('mas', gray)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()