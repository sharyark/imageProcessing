
from unittest import result
import cv2
print(cv2.__version__)

class mpFace:
    import mediapipe as mp
    def __init__(self):
        self.myFace = self.mp.solutions.face_detection.FaceDetection()
    def Marks(self,frm):
        frameRGB = cv2.cvtColor(frm,cv2.COLOR_BGR2RGB)
        result = self.myFace.process(frameRGB)
        faceBoundBoxs = []
        if result.detections != None:
            for face in result.detections:
                bBox = face.location_data.relative_bounding_box
                topLeft = (int(bBox.xmin*width),int(bBox.ymin*height))
                bottomRight = (int((bBox.xmin+bBox.width)*width),int((bBox.ymin+bBox.height)*height))
                # print('this is bottom',bottomRight)
                # print('bbox.widht',bBox.width)
                # print('bbox.height',bBox.height)
                faceBoundBoxs.append((topLeft,bottomRight))
        return faceBoundBoxs    

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
        handTpyes = []
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=self.hands.process(frameRGB)
        if results.multi_hand_landmarks != None:
            for thand in results.multi_handedness:
                handtype = thand.classification[0].label
                handTpyes.append(handtype)
            for handLandMarks in results.multi_hand_landmarks:
                myHand=[]
                for landMark in handLandMarks.landmark:
                    myHand.append((int(landMark.x*width),int(landMark.y*height)))
                myHands.append(myHand)
        return myHands,handTpyes

width=800
height=400
# cam=cv2.VideoCapture(0)
cam = cv2.VideoCapture('http://192.168.1.10:4747/video')

cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
# cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
handObj = mpHands()
bodyPos = mpPose()
facePos = mpFace()
while True:
    ignore,  frame = cam.read()
    frame=cv2.resize(frame,(width,height))
    handData,handtypes=handObj.Marks(frame)
    posData = bodyPos.Marks(frame)
    facexy = facePos.Marks(frame)
    print(facexy)
    # cv2.circle(frame,posData[5],25,(255,0,255),3)
    if len(facexy) > 0:
        cv2.rectangle(frame,facexy[0][0],facexy[0][1],(0,212,200),3)  
    for hand in handData:
        for ind in [0,5,6,7,8]:
            cv2.circle(frame,hand[ind],25,(255,0,255),3)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()