from asyncio import events
from os import getloadavg
import time
import cv2
width = 640
height = 360
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
evt = 0
def mouseClick(event,x,y,flag,param):
    global pnt
    global pnt1
    global evt
    if event == cv2.EVENT_LBUTTONDOWN:
        pnt = (x,y)
        evt = event
        print("event of Lbuttondown number is :",event)
        # print(pnt)
        print("left button up pos:",x,y)
    if event == cv2.EVENT_LBUTTONUP:
        pnt1 = (x,y)
        print("event of Lbuttonup number is :",event)
        print("left button up pos:",x,y)
        evt = event
cv2.namedWindow('webcam1')
cv2.setMouseCallback('webcam1',mouseClick)
a = 0
while True:
    _, frame = cam.read()
    if evt == 4 or a==1:
        cv2.rectangle(frame,pnt,pnt1,(234,122,200),2)
        frm = frame[pnt[1]:pnt1[1],pnt[0]:pnt1[0]] # this take as y(row) value and x(col) value
        cv2.imshow('small',frm)
    cv2.imshow('webcam1',frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()