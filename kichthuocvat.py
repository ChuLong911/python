import cv2
import numpy as np
#doc anh vaf hien thi
video = cv2.VideoCapture('http://192.168.1.29:8080/video')#

while(True):
    ret,frame = video.read()
    cap = cv2.resize(frame, (600, 500))

    # chuyen anh thanh anh xam va phan nguong
    gray = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)

    cap_blur = cv2.GaussianBlur(gray,(11,11), -1)

   # _,thresh = cv2.threshold(cap_blur, 160, 255, cv2.THRESH_BINARY_INV)[1]
    _, thresh = cv2.threshold(cap_blur, 160, 255, cv2.THRESH_BINARY_INV)

    # tim hinh anh co duong vien lon nhat cua anh da phan nguong
    cnts,_ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        area = cv2.contourArea(contour)
        if area > 1000:
            #tim hinh nho nha
            rect = cv2.minAreaRect(contour)
            rect_width, rect_height = rect[1]
            rect_pts = cv2.boxPoints(rect)
            rect_pts = np.intp(rect_pts)
            #tim 4 diem hinh bo
            cv2.putText(cap, "1", rect_pts[0], cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0),2)
            cv2.putText(cap, "2", rect_pts[1], cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0),2)
            cv2.putText(cap, "3", rect_pts[2], cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0),2)
            cv2.putText(cap, "4", rect_pts[3], cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0),2)
            #in hinh chu nhat bo len man hinh
            cv2.drawContours(cap, [rect_pts], -1, (0, 255, 0),2)

            #quy doi pixel ---> mm (863px = 200mm)
            kt_real = 200/863.3

            text_height = f"{round(rect_height*kt_real), 2}"
            text_width = f"{round(rect_width*kt_real), 2}"

            #tinh toan vitri der hien thi text kich thuoc cua hcn
            txt_height_position = ((rect_pts[0][0] + rect_pts[1][0])//2, (rect_pts[1][1] + rect_pts[2][1]) //2 )
            txt_width_position = ((rect_pts[1][0] + rect_pts[2][0]) // 2, (rect_pts[1][1] + rect_pts[2][1]) // 2)

            cv2.putText(cap,text_height, txt_height_position, cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255), 2)
            cv2.putText(cap,text_width, txt_width_position,cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            print('kt', text_height)

            print('kt', text_width )
    cv2.imshow('app', cap)
    cv2.imshow("thresh", thresh)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
video.release()
cv2.destroyAllWindows()


