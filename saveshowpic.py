import cv2
path = r'D:\anhchun.jpg'
img= cv2.imread(path,1)
cv2.imshow('hien_anh',img)
cv2.imwrite('a1.jpg',img)
#cv2.imwrite()
cv2.waitKey(0)
#cv2.destroyWindow()
