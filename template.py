import numpy as np
import cv2

cap = cv2.VideoCapture('http://192.168.1.10:4747/video')

while(True):
    ret, frame = cap.read()

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()









# import cv2
# print(cv2.__version__)
# width = 640
# height = 360
# cam = cv2.VideoCapture('http://192.162.1.10:8080/video')
# cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
# cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
# while True:
#     ignore , frame = cam.read()
#     cv2.imshow('name1', frame)
#     if cv2.waitKey(1) == ord('q'):
#         break
# cam.release()
