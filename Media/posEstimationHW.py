import re
from turtle import width
import cv2
print(cv2.__version__)

class mpPose:
    import mediapipe as mp
    def __init__(self,still=False,upperBody = False,smoothData = True):
        self.myPose = self.mp.solutions.pose.Pose()
    def Marks(self,frame):
        frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results = self.myPose.process(frameRGB)
        landMarkd = []
        if results.pose_landmarks:
            for lm in results.pose_landmarks.landmark:
                landMarkd.append((int(lm.x*width),int(lm.y*height)))
        return landMarkd
class mpHands:
    import mediapipe as mp
    def __init__(self,maxHands=2,tol1=1,tol2=.5):
        self.hands=self.mp.solutions.hands.Hands(False,maxHands,tol1,tol2)
    def Marks(self,frame):
        myHands=[]
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=self.hands.process(frameRGB)
        if results.multi_hand_landmarks != None:
            for handLandMarks in results.multi_hand_landmarks:
                myHand=[]
                for landMark in handLandMarks.landmark:
                    myHand.append((int(landMark.x*width),int(landMark.y*height)))
                myHands.append(myHand)
        return myHands

width=800
height=400
cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
findHands=mpHands(2)
bodyPos = mpPose()
while True:
    ignore,  frame = cam.read()
    frame=cv2.resize(frame,(width,height))
    handData=findHands.Marks(frame)
    posData = bodyPos.Marks(frame)
    cv2.circle(frame,posData[0],25,(255,0,255),3)

    for hand in handData:
        for ind in [0,5,6,7,8]:
            cv2.circle(frame,hand[ind],25,(255,0,255),3)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()