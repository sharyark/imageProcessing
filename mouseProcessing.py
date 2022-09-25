import time
import cv2
width = 640
height = 360
evt = 0
pnt = ()
def mouseClick(event,xp,yp,flag,param):
    print('mouse is detecting')
    global pnt
    # global pnt1
    global evt
    evt = event
    if event == cv2.EVENT_RBUTTONDOWN:
        pnt = (xp,yp)
        evt = event
        print(evt)
        # print('right is down',xp,yp)  
        # display that left button 
        # was clicked.

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cv2.namedWindow('webcam')
cv2.setMouseCallback('webcam',mouseClick)
font = cv2.FONT_HERSHEY_TRIPLEX
LB = 'Left Button'
while True:
    _, frame = cam.read()
    if evt == 4 or evt ==1:
        x,y = pnt
        cv2.putText(frame, LB, (x, y),font, 1, (255, 255, 0), 2) 
        print("debugingg")
        print(evt)
    cv2.imshow('webcam',frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()

# def mouseClick(event,xp,yp,flag,param):
    # print('mouse is detecting')