from re import A
import cv2
print(cv2.__version__)

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
circleX = 100
circleY = 0
deltaX = 4
deltaY = 4
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
# cam.set(cv2.CAP_PROP_FPS, 30)
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
findHands=mpHands(2)
paddleWidth = 100
paddleHeight = 30
paddleColor = (0,243,166)
while True:
    ignore,  frame = cam.read()
    frame=cv2.resize(frame,(width,height))
    handData=findHands.Marks(frame)
    for hand in handData:
        cv2.rectangle(frame,(int(hand[8][0]-paddleWidth/2),0),(hand[8][0]+paddleWidth,paddleHeight),paddleColor,-1)
        # cv2.rectangle(frame,(hand[8][0],hand[8][1]),(hand[8][0]+paddleWidth,hand[8][1]+paddleHeight),paddleColor,-1)
        # if hand[8][0] == circleX:
        if circleX+25 >= width or circleX+25 <= 0:
            deltaX *= -1
        if circleY >= height :
            deltaY *= -1
        x1 = hand[8][0]
        y1 = hand[8][0]+paddleWidth
        print('x  :',x1)
        print('y  :',y1)
        print('----')
        if circleY <= paddleHeight:
            if circleX >= hand[8][0] and circleX <= hand[8][0]+paddleWidth:
                deltaY *= -1
        circleX = circleX+deltaX
        circleY = circleY+deltaY
        cv2.circle(frame,(circleX,circleY),25,(0,123,222),3)
        # else:
            # pass
        cv2.putText(frame,str(hand[8][0]),(200, 200),cv2.FONT_HERSHEY_DUPLEX,3.0,(125, 246, 55),3)
        cv2.putText(frame,str(circleX),(400, 400),cv2.FONT_HERSHEY_DUPLEX,3.0,(125, 246, 55),3)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()



























# import cv2
# print(cv2.__version__)

# class mpHands:
#     import mediapipe as mp
#     def __init__(self,maxHands=2,tol1=1,tol2=.5):
#         self.hands=self.mp.solutions.hands.Hands(False,maxHands,tol1,tol2)
#     def Marks(self,frame):
#         myHands=[]
#         frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
#         results=self.hands.process(frameRGB)
#         if results.multi_hand_landmarks != None:
#             for handLandMarks in results.multi_hand_landmarks:
#                 myHand=[]
#                 for landMark in handLandMarks.landmark:
#                     myHand.append((int(landMark.x*width),int(landMark.y*height)))
#                 myHands.append(myHand)
#         return myHands
# width=1280
# height=520
# cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
# cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
# cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
# # cam.set(cv2.CAP_PROP_FPS, 30)
# cam = cv2.VideoCapture(0)
# cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
# findHands=mpHands(2)
# paddleWidth = 100
# paddleHeight = 30
# paddleColor = (0,243,166)
# while True:
#     ignore,  frame = cam.read()
#     frame=cv2.resize(frame,(width,height))
#     handData=findHands.Marks(frame)
#     for hand in handData:
#         cv2.rectangle(frame,(int(hand[8][0]-paddleWidth/2),0),(hand[8][0]+paddleWidth,paddleHeight),paddleColor,-1)
#         # cv2.rectangle(frame,(hand[8][0],hand[8][1]),(hand[8][0]+paddleWidth,hand[8][1]+paddleHeight),paddleColor,-1)
#     cv2.imshow('my WEBcam', frame)
#     cv2.moveWindow('my WEBcam',0,0)
#     if cv2.waitKey(1) & 0xff ==ord('q'):
#         break
# cam.release()