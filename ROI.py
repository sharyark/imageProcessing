import time
import cv2
width = 640
height = 360
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
while True:
    _, frame = cam.read()
    frameROI = frame[100:220,260:380] # this much part i took as ROI
    grayroi = cv2.cvtColor(frameROI,cv2.COLOR_BGR2GRAY)
    bgrroi = cv2.cvtColor(grayroi,cv2.COLOR_GRAY2BGR)
    frame[0:120,0:120] = bgrroi
    cv2.imshow('roi',frameROI)
    cv2.imshow('roiGRY',grayroi)
    cv2.imshow('webcam',frame)
    cv2.moveWindow('webcam',0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()