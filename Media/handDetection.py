import cv2
import mediapipe as mp
print(cv2.__version__)
width = 640
height = 360
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
hands = mp.solutions.hands.Hands(False,2,1,.5,.5)
mpDraw = mp.solutions.drawing_utils
while True:
    ignore , frame = cam.read()
    frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results = hands.process(frameRGB)
    if results.multi_hand_landmarks != None:
        for handLandMarks in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(frame,handLandMarks,mp.solutions.hands.HAND_CONNECTIONS)
            for landmark in handLandMarks.landmark:
                print(landmark.x)
            # print(handLandMarks.landmark.x,handLandMarks.landmark.y)

    cv2.imshow('name1', frame)
    # print(type(results.multi_hand_landmarks))
    if cv2.waitKey(1) == ord('q'):
        break
cam.release()
