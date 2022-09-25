import time
import cv2
width = 640
height = 360
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
snipw = 100
sniph = 80

boxcr = int(sniph/2)
boxcc = int(snipw/2)

deltar = 1
deltac = 1
while True:
    _, frame = cam.read()
    roi = frame[boxcr-int(sniph/2):boxcr+int(sniph/2),boxcc-int(snipw/2):boxcc+int(snipw/2)]
    # frameg = frame[:,:]
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame = cv2.cvtColor(frame,cv2.COLOR_GRAY2BGR)
    frame[boxcr-int(sniph/2):boxcr+int(sniph/2),boxcc-int(snipw/2):boxcc+int(snipw/2)] = roi
    cv2.imshow('webcam1',frame)
    cv2.imshow('webcam',roi)
    boxcr += deltar 
    boxcc += deltac 
    if boxcr-int(sniph/2) <= 0 or boxcr+int(sniph/2) >= height:
        deltar = deltar * (-1)
    if boxcc-int(snipw/2) <= 0 or boxcc+int(snipw/2) >= width:
        deltac = deltac * (-1)
    # cv2.moveWindow('webcam',,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()