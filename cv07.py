import imp


import time
import cv2
width = 640
height = 360
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
a = 0
b = 0
while True:
    a = time.time()
    _, frame = cam.read()
    # frame[1:100,1:100] = (90,90,90)
    # frame[1:100,540:] = (90,90,90)
    # cv2.rectangle(frame,(150,100),(250,200),(0,0,200),50)   #frame the x y for uper point then x,y for lower point then color then tickness for solid -1
    # cv2.putText(frame,"sharyar khan",(1,150),cv2.FONT_HERSHEY_COMPLEX,2,(255,0,0),2)
    cv2.imshow('webcam',frame)
    cv2.moveWindow('webcam',0,0)
    b = time.time()
    print(1/(b-a))
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()