# lecture no 7
# import imp
import cv2
import numpy as np
# print(cv2.__version__)
cam = cv2.VideoCapture(0) # making camera object
frame1 = np.zeros([5,5,3])
frame1[:,:] = (123,200,152)
print(frame1)
while True:
    ignore , frame = cam.read()
    # cv2.imshow('name', frame)
    cv2.imshow('name', frame1)
    if cv2.waitKey(1) == ord('q'):
        break
cam.release()

# frame = np.ones([4,5])
# frame[1:2,2:4] = 7
# print(frame[1:3,:])