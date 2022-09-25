import errno
import cv2
print(cv2.__version__)
import numpy as np

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
def findDistances(handData):
    distMatrix=np.zeros([len(handData),len(handData)],dtype='float')
    palmSize = ((handData[0][0]-handData[9][0])**2+(handData[0][1]-handData[9][1])**2)**(1./2.)
    for row in range(0,len(handData)):
        for column in range(0,len(handData)):
            distMatrix[row][column]=(((handData[row][0]-handData[column][0])**2+(handData[row][1]-handData[column][1])**2)**(1./2.))/palmSize
    return distMatrix

def findError(gestureMatrix,unknownMatrix,keyPoints):
    error=0
    for row in keyPoints:
        for column in keyPoints:
            error=error+abs(gestureMatrix[row][column]-unknownMatrix[row][column])
    return error
def findGesture(known,unknow,keypoint,gestName,tol):
    errorArray = []
    for i in range(len(gestName)):
        error = findError(known[i],unknow,keypoint)
        errorArray.append(error)
    minerror = errorArray[0]
    minIndex = 0
    for i in range(len(errorArray)):
        if errorArray[i] < minerror:
            minerror = errorArray[i]
            minIndex = i
    if tol > minerror:
        gesture = gestName[minIndex]
    else:
        gesture = 'unknown'
    return gesture
width=1080
height=520
cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
findHands=mpHands(1)

keyPoints=[0,4,5,9,13,17,8,12,16,20]
train=True
tolr = 1500
traincnt = 0
knownGestures = []
numGest = int(input('howManyGestureDoYouWant'))

namGesture = []
for i in range(numGest):
    name = input('enter gesture number '+str(i+1)+' ')
    namGesture.append(name)
print(namGesture)

while True:
    ignore,  frame = cam.read()
    frame=cv2.resize(frame,(width,height))
    handData=findHands.Marks(frame)
    if train==True:
        if handData!=[]:
            print('Show your Gesture, '+namGesture[traincnt] + ': press t to ready')
            if cv2.waitKey(1) & 0xff==ord('t'):
                knownGesture=findDistances(handData[0])
                knownGestures.append(knownGesture)
                traincnt += 1
                if traincnt == numGest:
                    train = False
                # print(knownGesture)
    if train == False:
        if handData!=[]:
            unknownGesture=findDistances(handData[0])
            myGesture = findGesture(knownGestures,unknownGesture,keyPoints,namGesture,tolr)
            # error=findError(knownGestures,unknownGesture,keyPoints)
            cv2.putText(frame,str(myGesture),(100,175),cv2.FONT_HERSHEY_SIMPLEX,3,(255,0,0),8)
    for hand in handData:
        for ind in keyPoints:
            cv2.circle(frame,hand[ind],25,(255,0,255),3)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()
