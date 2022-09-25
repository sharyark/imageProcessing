import numpy as np
import cv2
print(cv2.__version__)

def findDistance(handData):
    distMatrix = np.zeros([len(handData),len(handData)],dtype='float')
    for row in range(0,len(handData)):
        for column in range(0,len(handData)):
            distMatrix[row][column] = ((handData[row][0]-handData[column][0])**2+(handData[row][0]-handData[column][0])**2)**.5
    return distMatrix

def findError(gestureMatrix,unknownMatrix,keypoints):
    error = 0
    for row in keyPoint:
        for col in keyPoint:
            error += abs(gestureMatrix[row][col]-unknownMatrix[row][col])
    return error

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

width=1280
height=620
# cam = cv2.VideoCapture('http://192.168.1.10:4747/video')

cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
findHands=mpHands(2)
train = True
keyPoint = [0,4,5,9,13,17,8,12,16,20]
knownGesture = []
while True:
    ignore,  frame = cam.read()
    frame=cv2.resize(frame,(width,height))
    handData=findHands.Marks(frame)
    if train == True:
        if handData != []:
            print('enter t')
            if cv2.waitKey(1) & 0xff==ord('t'):
                knownGesture = findDistance(handData[0])
                print(knownGesture)
                train = False
    if train == False:
        if handData != []:
            unknowngesture = findDistance(handData[0])
            error = findError(knownGesture,unknowngesture,keyPoint)
            cv2.putText(frame,str(int(error)),(100,100),cv2.FONT_HERSHEY_SIMPLEX,3,(222,111,222),8)
    # for hand in handData:
    #     for ind in keyPoint:
    #         cv2.circle(frame,hand[ind],25,(255,0,255),3)
    # tmp = []
    # for i in keyPoint:
    #     if len(handData) > 0:
    #         tmp.append(handData[0][i])
    # print(len(findDistance(tmp)))
    # print(len(handData))
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()