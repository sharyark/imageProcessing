

# from secrets import randbelow
import cv2
import numpy as np
row = 80
coulmn = 60
cam = cv2.VideoCapture(0) # making camera object
frame1 = np.zeros([row,coulmn])
# frame1[:,112:3] = 1 
check = 1
area = int((row*coulmn)/20)
print(area)
rs=0
cs = 0
for i in range(row):
    # print(i)
    for j in range(coulmn):
        if check > 0:
            frame1[i:i+area,j:j+area] = 0
            check *= -1
            print('if....')
            print(check)
            
        else:
            print('else....')
            frame1[i:i+area,j:j+area] = 1
            check *= -1
    check *= -1
print(frame1)
while True:
    ignore , frame = cam.read()
    cv2.imshow('name', frame1)
    if cv2.waitKey(1) == ord('q'):
        break
cam.release()
