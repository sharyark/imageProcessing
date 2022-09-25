import cv2
print(cv2.__version__)
width = 640
height = 360
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)

# faceCascade = cv2.CascadeClassifier('/home/shary/Desktop/AI/paul/face/haar/haarcascade_frontalface_default.xml')
faceCascade = cv2.CascadeClassifier('/home/shary/Desktop/AI/paul/face/haar/haarcascade_eye.xml')

while True:
    ignore , frame = cam.read()
    grayFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(grayFrame,1.3,5)
    for face in faces:
        x,y,w,h = face
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,143,122),5)
    cv2.imshow('name1', frame)
    if cv2.waitKey(1) == ord('q'):
        break
cam.release()
