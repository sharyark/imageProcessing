import cv2
print(cv2.__version__)
cam = cv2.VideoCapture(0) # making camera object
while True:
    ignore , frame = cam.read()
    cv2.imshow('name', frame)
    if cv2.waitKey(1) == ord('q'):
        break
cam.release()
