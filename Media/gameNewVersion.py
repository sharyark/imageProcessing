import cv2
print(cv2.__version__)
class mpHands:
    import mediapipe as mp
    def __init__(self,maxHands=2,tol1=1,tol2=.5):
        self.hands=self.mp.solutions.hands.Hands(False,maxHands,tol1,tol2)
    def Marks(self,frame):
        myHands=[]
        myhands = []
        handTypes = []
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=self.hands.process(frameRGB)
        if results.multi_hand_landmarks != None:
            for thand in results.multi_handedness:
                handtype = thand.classification[0].label
                handTypes.append(handtype)
            for handLandMarks in results.multi_hand_landmarks:
                myHand=[]
                for landMark in handLandMarks.landmark:
                    myHand.append((int(landMark.x*width),int(landMark.y*height)))
                myHands.append(myHand)
        return myHands,handTypes
width=600
height=400
circleX = 100
circleY = 0
deltaX = 6
deltaY = 6
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
findHands=mpHands(2)
paddleWidth = 50
paddleHeight = 30
paddleColor = (0,243,166)
circleColor = (0,0,0)
# tmp1 = (hand[8][0]-paddleWidth,0)
# tmp2 = (hand[8][0]+paddleWidth,paddleHeight)
x = 0
tmp1 = 0
while True:
    ignore,  frame = cam.read()
    frame=cv2.resize(frame,(width,height))
    handData,handtype=findHands.Marks(frame)
    for hand,typeOfHand in zip(handData,handtype):
        
        if typeOfHand == 'Right':
            circleColor = (0,0,255)
            if hand[8][0] < tmp1:
                x = hand[8][0]
                print('debuggg')
            print(typeOfHand)
        if typeOfHand == 'Left':
            circleColor = (255,0,0)
            if hand[8][0] > tmp1:
                x = hand[8][0]       
        tmp1 = hand[8][0]
        cv2.rectangle(frame,(x-paddleWidth,0),(x+paddleWidth,paddleHeight),paddleColor,-1)
        if circleX+25 >= width or circleX-25 <= 0:
            deltaX *= -1
        if circleY+25 >= height :
            deltaY *= -1
        if circleY-25 <= paddleHeight:
            if circleX+10 >= hand[8][0]-paddleWidth and circleX-10 < hand[8][0]+paddleWidth:
                deltaY *= -1
                # print('debug...')
        circleX = circleX+deltaX
        circleY = circleY+deltaY
        cv2.circle(frame,(circleX,circleY),25,circleColor,3)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()

