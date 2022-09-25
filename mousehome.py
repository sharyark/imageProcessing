from asyncio import events
from os import getloadavg
import time
import cv2
# from mouseProcessing import mouseClick
width = 640
height = 360
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
evt = 0
# pnt1 = (0,0)
# pnt = (0,0)
def mouseClick(event,x,y,flag,param):
    global pnt
    global pnt1
    global evt
    if event == cv2.EVENT_LBUTTONDOWN:
        pnt = (x,y)
        evt = event
        print(pnt)
    if event == cv2.EVENT_LBUTTONUP:
        pnt1 = (x,y)
        print(pnt1)
        evt = event

# snipw = 100
# sniph = 80
# boxcr = int(sniph/2)
# boxcc = int(snipw/2)
# deltar = 1
# deltac = 1

cv2.namedWindow('webcam1')
cv2.setMouseCallback('webcam1',mouseClick)
global frm
frm = []
a = 0
while True:
    _, frame = cam.read()
    # roi = frame[boxcr-int(sniph/2):boxcr+int(sniph/2),boxcc-int(snipw/2):boxcc+int(snipw/2)]
    # frameg = frame[:,:]
    if evt == 4 or a==1:
        cv2.rectangle(frame,pnt,pnt1,(234,122,200),2)
        # a = 1
        frm = frame[pnt[1]:pnt1[1],pnt[0]:pnt1[0]] # this take as y(row) value and x(col) value
    # print(frm)  
        # print(a)
        cv2.imshow('small',frm)
        # print(123)
    # frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # frame = cv2.cvtColor(frame,cv2.COLOR_GRAY2BGR)
    # frame[boxcr-int(sniph/2):boxcr+int(sniph/2),boxcc-int(snipw/2):boxcc+int(snipw/2)] = roi
    cv2.imshow('webcam1',frame)
    # cv2.imshow('webcam',roi)
    # boxcr += deltar 
    # boxcc += deltac 
    # if boxcr-int(sniph/2) <= 0 or boxcr+int(sniph/2) >= height:
    #     deltar = deltar * (-1)
    # if boxcc-int(snipw/2) <= 0 or boxcc+int(snipw/2) >= width:
    #     deltac = deltac * (-1)
    # cv2.moveWindow('webcam',,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()