from typing import Counter
import cv2
import numpy as np
print(cv2.__version__)
width = 640
height = 360
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
x = np.zeros([256,600,3],dtype=np.uint8)
x = cv2.cvtColor(x,cv2.COLOR_BGR2HSV)
# x[:][:][:] = 255
# x[:][:][:] = 200
# here we are making hsv policy 
for i in range(1,255):
    # x[i][i][0] = i
    for j in range(0,180):
        x[i,j] = (j,i,i)

for i in range(0,255):
    # x[i][i][0] = i
    Counter = 0
    for j in range(180,360):
        x[i,j] = (Counter,i,255)
        Counter += 1
# so here we are backing hsv to bgr 
x = cv2.cvtColor(x,cv2.COLOR_HSV2BGR)
row = 0
while True:
    # ignore , frame = cam.read()
    # print(x[row][row])
    cv2.imshow('name1', x)
    row +=1
    # if row >= 350:
    #     break
    if cv2.waitKey(1) == ord('q'):
        break
cam.release()
