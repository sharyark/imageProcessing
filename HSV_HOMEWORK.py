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





















# import numpy as np
# import cv2
# print(cv2.__version__)
# width = 640
# height = 360
# evnt = 0
# xVal = 0
# yVal = 0
# def mouseClick1(event,xpos,ypos,flag,params):
#     global evnt
#     global xVal
#     global yVal
#     if event == cv2.EVENT_LBUTTONDOWN:
#         # print(event)
#         xVal = xpos
#         yVal = ypos
#         evnt = event
#     if event == cv2.EVENT_RBUTTONUP:
#         evnt = event
#         # print(event)

# cam = cv2.VideoCapture(0)
# cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
# cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
# cv2.namedWindow('name')
# cv2.setMouseCallback('name',mouseClick1)
# x = np.zeros([200,600,3],dtype=np.uint8)
# x = cv2.cvtColor(x,cv2.COLOR_BGR2HSV)
# while True:
#     ignore , frame = cam.read()
#     x = np.zeros([200,600,3],dtype=np.uint8)
#     y = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
#     if evnt == 1:
#         print("call back function is called")
#         print(x[yVal,xVal])
#         x[yVal,xVal][0] = 3

#         # print(x[yVal,xVal][0])
#         x[yVal,xVal][2] = 100
#         x[yVal,xVal][1] = 255

#         for i in range(0,170):
#             x[yVal,xVal][0] = i
#             cv2.imshow('name11',x)
#             print(x[yVal,xVal])
#         print(x)
#         y = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
#         Y1 = frame[yVal,xVal]
#         x[:,:] = frame[yVal,xVal]
#         cv2.imshow('name1',x)
#         print("hsv color is ",Y1)
#         evnt = 0
#     cv2.imshow('name', frame)
#     if cv2.waitKey(1) == ord('q'):
#         break
# cam.release()
