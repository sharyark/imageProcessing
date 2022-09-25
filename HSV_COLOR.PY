import imp


import numpy as np
import cv2
print(cv2.__version__)
width = 640
height = 360
evnt = 0
xVal = 0
yVal = 0
def mouseClick(event,xpos,ypos,flag,params):
    global evnt
    global xVal
    global yVal
    if event == cv2.EVENT_LBUTTONDOWN:
        print(event)
        xVal = xpos
        yVal = ypos
        evnt = event
    if event == cv2.EVENT_RBUTTONUP:
        evnt = event
        print(event)

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cv2.namedWindow('name')
cv2.setMouseCallback('name',mouseClick)
while True:
    ignore , frame = cam.read()
    if evnt == 1:
        x = np.zeros([250,250,3],dtype=np.uint8)
        clr = frame[yVal][xVal]
        # print(x)
        x [:,:]= clr
        cv2.imshow('color picker',x)
        cv2.moveWindow('color picker',width,0)
        print('this is clr ',clr)
        # print('this is x after clr',x)
        evnt = 0
    cv2.imshow('name', frame)
    if cv2.waitKey(1) == ord('q'):
        break
cam.release()
