import cv2
print(cv2.__version__)
cam = cv2.VideoCapture(0) # making camera object
while True:
    ignore , frame = cam.read()
    ignore1 , frame1 = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY )
    cv2.imshow('name', frame)
    # cv2.imshow('name1', frame1)
    cv2.imshow('name1', gray)
    if cv2.waitKey(1) == ord('q'):
        break
cam.release()
