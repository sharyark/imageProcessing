# from ctypes import sizeof
# from ctypes.wintypes import HMODULE
# from turtle import shape
import numpy as np
import cv2
print(cv2.__version__)
width = 640
height = 360

def onTrack1(val):
    global heulow
    heulow = val
    # print('heu low ',heulow)

def onTrack2(val):
    global heuhigh
    heuhigh = val
    # print('heu high ',heuhigh)

def onTrack3(val):
    global satlow
    satlow = val
    # print('sat low ',satlow)

def onTrack4(val):
    global sathigh
    sathigh = val
    # print('sat high ',sathigh)

def onTrack5(val):
    global vallow
    vallow = val
    # print('val low ',vallow)
def onTrack1_1(val):
    global heulow1
    heulow1 = val

def onTrack2_1(val):
    global heuhigh1
    heuhigh1 = val

def onTrack6(val):
    global valhigh
    valhigh = val
    # print('val high ',valhigh)

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
heulow = 10
heuhigh = 25
heulow1 = 10
heuhigh1 = 25
satlow = 30
sathigh = 60
vallow = 30
valhigh = 80
cv2.namedWindow('myTrackbar')
cv2.moveWindow('mytracker',width,0)
cv2.resizeWindow('myTracbar',100,300)
cv2.createTrackbar('Heu low','myTrackbar',10,179,onTrack1)
cv2.createTrackbar('Heu high','myTrackbar',10,179,onTrack2)
cv2.createTrackbar('Heu low1','myTrackbar',10,179,onTrack1_1)
cv2.createTrackbar('Heu high1','myTrackbar',10,179,onTrack2_1)
cv2.createTrackbar('sat low','myTrackbar',10,179,onTrack3)
cv2.createTrackbar('sat high','myTrackbar',10,179,onTrack4)
cv2.createTrackbar('val low','myTrackbar',10,179,onTrack5)
cv2.createTrackbar('val high','myTrackbar',10,179,onTrack6)

while True:
    ignore , frame = cam.read()
    framehsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    uprBound = np.array([heuhigh,sathigh,valhigh])
    lwrBound = np.array([heulow,satlow,vallow])
    
    uprBound1 = np.array([heuhigh1,sathigh,valhigh])
    lwrBound1 = np.array([heulow1,satlow,vallow])
    
    masked = cv2.inRange(framehsv,lwrBound,uprBound)
    masked1 = cv2.inRange(framehsv,lwrBound1,uprBound1)

    compositmask = masked | masked1
    # masked = cv2.bitwise_not(masked)
    # print("this is mask ------------",masked1)
    # print("this is type of mask ------------",masked1.shape)
    scanedObj = cv2.bitwise_and(frame,frame,mask=compositmask)
    scanedObj1 = cv2.cvtColor(scanedObj,cv2.COLOR_HSV2BGR)
    cv2.imshow('masked',masked) 
    cv2.imshow('masked1',masked1) 
    cv2.imshow('scanedObject',scanedObj)
    cv2.imshow('mainFrame', frame)
    cv2.moveWindow('name1',0,0)
    cv2.moveWindow('name',0,height)
    if cv2.waitKey(1) == ord('q'):
        break
cam.release()
# 45:00 lecture 22 video