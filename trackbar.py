# from logging import getLoggerClass
# from turtle import circle
from cv2 import *
print(cv2.__version__)
width = 640
height = 360
myRed = 25
xPos = int(width/2)
ypos = int(height/2)
def myCallBack1(val):
    # print(val)
    global xPos
    xPos = val
def myCallBack2(val):
    # print(val)
    global ypos
    ypos = val
cam = VideoCapture(0)
cam.set(CAP_PROP_FRAME_WIDTH,width)
cam.set(CAP_PROP_FRAME_HEIGHT,height)
namedWindow('myTrackbars')
resizeWindow('myTrackbars',400,100)
createTrackbar('xPos','myTrackbars',int(width/2),640,myCallBack1)
createTrackbar('yPos','myTrackbars',int(width/2),360,myCallBack2)
while True:
    ignore , frame = cam.read()
    circle(frame,(xPos,ypos),myRed,(255,0,0),2)
    imshow('name1', frame)
    if waitKey(1) == ord('q'):
        break
cam.release()
