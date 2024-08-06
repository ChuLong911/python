import cv2 as cv
import numpy as np
#https://www.youtube.com/watch?v=8d14UPLGiPc
def dectect_colored_objects(frame):
    #chuyển dổi hình từ bgr sang hsv
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    #xac dinh khoang gia trị mau trong hsv bằng colorpicker/ chia doi thon so dau
    #https://colorpicker.me/#feff00
    lower_yellow = np.array([20,100, 100])
    upper_yellow = np.array([30,255, 255])

    lower_whitemilk = np.array([20, 100, 100])
    upper_whitemilk = np.array([30, 8, 87])

    lower_blue = np.array([90, 100, 100])
    upper_blue = np.array([120, 255, 255])

    #tao mask de chi giu lai pixel mau nam trong vung gt xac dinh
    mask_y = cv.inRange(hsv, lower_yellow, upper_yellow)
    mask_w = cv.inRange(hsv, lower_whitemilk, upper_whitemilk)
    mask_b = cv.inRange(hsv, lower_blue, upper_blue)

    #tim contour vung mau can xd
    contour_y, _= cv.findContours(mask_y, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    contour_w, _= cv.findContours(mask_w, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    contour_b, _= cv.findContours(mask_b, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    #duyet contour vaf ve duong vien bouding box
    for contour in contour_y:
        area = cv.contourArea(contour)
        if area > 1000:
            x, y, w, h = cv.boundingRect(contour)
            cv.rectangle(frame, (x, y), (x + w, y + h), (0,255,0), 2)
            cv.putText(frame, "yellow", (x, y -15), cv.FONT_HERSHEY_SIMPLEX, 1 , (0,255,0),2)

    for contour in contour_w:
        area = cv.contourArea(contour)
        if area > 1000:
            x, y, w, h = cv.boundingRect(contour)
            cv.rectangle(frame, (x, y), (x + w, y + h), (226,226,20), 2)
            cv.putText(frame, "white milk", (x, y -15), cv.FONT_HERSHEY_SIMPLEX, 1 , (226,226,20),2)

    for contour in contour_b:
        area = cv.contourArea(contour)
        if area > 1000:
            x, y, w, h = cv.boundingRect(contour)
            cv.rectangle(frame, (x, y), (x + w, y + h), (255,0,0), 2)
            cv.putText(frame, "blue", (x, y -15), cv.FONT_HERSHEY_SIMPLEX, 1 , (255,0,0),2)

    return frame
def main():
    #mo camera
    video = cv.VideoCapture(0)#'http://192.168.1.29:8080/video'
    while True:
        ret,frame = video.read()
        #cap = cv.resize(frame, (600, 500))
        #phat hien vat co mau dang set
        colored_objects = dectect_colored_objects(frame)
        #hien  thi frame goc
        cv.imshow('app', dectect_colored_objects(frame))
        #thoat kho vong lap an "q"
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    #dong connect webcam va window hien thi
    video.release()
    cv.destroyAllWindows()

#if __name__ == "__main__":
   # main()