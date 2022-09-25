from lib2to3.pytree import Node
import cv2
import mediapipe as mp
print(cv2.__version__)
width = 640
height = 360
# cam = cv2.VideoCapture(0)
cam = cv2.VideoCapture('http://192.168.1.10:4747/video')

cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
findFace = mp.solutions.face_detection.FaceDetection()
mpDraw = mp.solutions.drawing_utils
while True:
    ignore , frame = cam.read()
    frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results = findFace.process(frameRGB)
    if results.detections != None:
        for face in results.detections:
            mpDraw.draw_detection(frame,face)


    # print(results.detections[0].location_data)
    cv2.imshow('name1', frame)
    if cv2.waitKey(1) == ord('q'):
        break
cam.release()
