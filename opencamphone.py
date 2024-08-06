import cv2
video = cv2.VideoCapture('http://192.168.1.29:8080/video')#
while (True):
   ret, frame = video.read()
   resize_fr = cv2.resize(frame,(600,500))
   cv2.imshow("frame",resize_fr)
   if cv2.waitKey(1) &0xFF == ord("q"):
     break
video.release()
cv2.destroyAllWindow()
