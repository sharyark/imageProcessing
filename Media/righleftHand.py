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

def handParsing(frm):
    frameRGB = cv2.cvtColor(frm,cv2.COLOR_BGR2RGB)
    myhands = []
    handTpyes = []
    results = hands.process(frameRGB)
    if results.multi_hand_landmarks != None:
        for thand in results.multi_handedness:
            handtype = thand.classification[0].label
            handTpyes.append(handtype)
        print(handTpyes)
        for handLandMarks in results.multi_hand_landmarks:
            myhand = []
            # # mpDraw.draw_landmarks(frame,handLandMarks,mp.solutions.hands.HAND_CONNECTIONS)
            for landmark in handLandMarks.landmark:
                myhand.append((int(landmark.x*width),int(landmark.y*height)))
            myhands.append(myhand)
    return myhands,handTpyes
# handFunObj = Hand()
while True:
    
    ignore , frame = cam.read()
    handp,handtypes = handParsing(frame)   #this is using function
    # print(len(handp))
    for handone,handT in zip(handp,handtypes):
        if handT == 'Right':
            circle_color = (0,0,252)
        elif handT == 'Left':
            circle_color = (255,0,0)
        cv2.circle(frame,handone[4],25,circle_color,3)
    cv2.imshow('name1', frame)
    if cv2.waitKey(1) == ord('q'):
        break
cam.release()

