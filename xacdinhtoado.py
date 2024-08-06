import cv2
import numpy as np

cv2.drawContours(frame, [c], 0, (255,0,255), 2)
M = cv2.moments(c)
cx = int(M["m10"]/(M["m00"])+0.1)
y = int(M["m01"]/(M["m00"])+0.1)
cv2.circle(frame, (cx,cy),7,(0,0,255), -1)
cv2.putText(frame, "Spoon:", (cx+9, cy+5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,1))
cv2.putText(frame, str(int(i)), (cx + 65, cy+5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 1))

cv2.putText(frame,"X=",  (cx-22, cy-16),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),1)
cv2.putText(frame,str(int(cx)), (cx+12, cy-16),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),1)
cv2.putText(frame,"Y=", (cx-22, cy+23),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),1)
cv2.putText(frame,str(int(cy)), (cx+12, cy+23),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),1)

#draw box arrow spoon
rect = cv2.minAreaRect(c)

          #  fit elipse
_, _, angle = cv2.fitEllipse(c)
P1x = cx
P1y = cy
length = 35
#calculate vector line at angle of bounding box
P2x = int(P1x + length * math.cos(math.radians(angle)))
P2y = int(P1y + length * math.sin(math.radians(angle)))
# draw vector line
cv2.line(frame, (cx, cy), (P2x, P2y), (255, 255, 255), 5)
 # output center of contour
print(P1x, P2y, angle)

cv2.putText(frame, "Angle=", (cx -100, cy + 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 1))
cv2.putText(frame, str(int(angle)), (cx - 45, cy + 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 1))

box = np.int0(cv2.boxPoints(rect))
cv2.drawContours(frame, [box], 0, (255, 255, 255), 2)

#draw vecto 0 degree
start = (cx,cy)
end = (cx,cy-60)
color = (0,0,255)
frame = cv2.line(frame,start,end,color,1)
#draw line pass throw center
rows, cols = frame.shape[:2]
[vx, vy, x, y] = cv2.fitLine(c, cv2.DIST_L2, 0, 0.01, 0.01)
lefty = int((-x * vy / vx) + y)
righty = int(((cols - x) * vy / vx) + y)
cv2.line(frame, (cols, righty), (cx, cy), (0, 0, 255), 1)
cv2.line(img, (cols - 1, righty), (0, lefty), (0, 255, 0), 2)

cv2.imshow("frame",frame)
k = cv2.waitKey(10)
if k == 27:
    break
cap.release()
cv2.destroyAllWindows()