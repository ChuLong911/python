import cv2 as cv
import numpy as np
import imutils

#doc anh vaf hien thi
#video = cv.VideoCapture('http://192.168.1.29:8080/video')
#image = cv.imread("phone.jpg")
while(True):
    #ret,frame = video.read()
    #image= cv.resize(frame, (600, 500))
    image = cv.imread("a2.PNG")
    cv.imshow("image", image)
#cv.waitKey(0)
#chuyen anh thanh anh xam va phan nguong
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    thresh = cv.threshold(gray,200,255,cv.THRESH_BINARY_INV)[1]
    cv.imshow("thresh", thresh)

#tim hinh anh co duong vien lon nhat cua anh da phan nguong
    cnts = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    c = max(cnts, key = cv.contourArea)
#ve duong vien vao anh
    output = image.copy()
    cv.drawContours(output, [c], -1, (0, 255, 0), 2)
    (x, y, w, h) = cv.boundingRect(c)
    text = "goc,N={}".format(len(c))
    cv.putText(output,text,(x-20, y), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
#show the original contour image
    print("thong tin: {}".format(text))
    cv.imshow("duong vien goc", output)
#pp xap xi duong vien
    for esp in np.linspace(0.0001, 0.001, 10):
        peri = cv.arcLength(c, True)
        approx = cv.approxPolyDP(c,esp * peri, True)
        #draw the approximated contour on the image
        output = image.copy()
        cv.drawContours(output, [approx], -1, (0,255,0), 2)
        text = "esp={:.4f},N={}".format(esp, len(approx))
        cv.putText(output, text, (x-20,y),cv.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255),2)

    #show approximated
        print("thong tin : {}".format(text))
        cv.imshow("xap xi", output)


    if cv.waitKey(1) & 0xFF == ord("q"):
        break
#video.release()
cv.destroyAllWindows()