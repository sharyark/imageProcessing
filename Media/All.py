import cv2
print(cv2.__version__)

class mpFaceMesh:
    import mediapipe as mp
    def __init__(self,still=False,numFaces=3,tol1=.5,tol2=.5,drawMesh=True):
        self.myFaceMesh=self.mp.solutions.face_mesh.FaceMesh()
        self.myDraw=self.mp.solutions.drawing_utils
        self.draw=drawMesh
    def Marks(self,frame,draw=True):
        global width
        global height
        drawSpecCircle=self.myDraw.DrawingSpec(thickness=0,circle_radius=0,color=(0,0,255))
        drawSpecLine=self.myDraw.DrawingSpec(thickness=1,circle_radius=1,color=(255,0,0))
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=self.myFaceMesh.process(frameRGB)
        facesMeshLandmarks=[]
        if results.multi_face_landmarks !=None:
            for faceMesh in results.multi_face_landmarks:
                faceMeshLandmarks=[]
                for lm in faceMesh.landmark:
                    loc=(int(lm.x*width),int(lm.y*height))
                    faceMeshLandmarks.append(loc)
                facesMeshLandmarks.append(faceMeshLandmarks)
                if draw==True:
                    self.myDraw.draw_landmarks(frame,faceMesh,self.mp.solutions.face_mesh.FACEMESH_CONTOURS,drawSpecCircle,drawSpecLine)
                    # self.myDraw.draw_landmarks(frame,faceMesh)
        return facesMeshLandmarks

class mpFace:
    import mediapipe as mp 
    def __init__(self):
        self.myFace=self.mp.solutions.face_detection.FaceDetection()
    def Marks(self,frame):
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=self.myFace.process(frameRGB)
        faceBoundBoxs=[]
        if results.detections != None:
            for face in results.detections:
                bBox=face.location_data.relative_bounding_box
                topLeft=(int(bBox.xmin*width),int(bBox.ymin*height))
                bottomRight=(int((bBox.xmin+bBox.width)*width),int((bBox.ymin+bBox.height)*height))
                faceBoundBoxs.append((topLeft,bottomRight))
        return faceBoundBoxs

class mpPose:
    import mediapipe as mp
    def __init__(self,still=False,upperBody=False, smoothData=True, tol1=.5, tol2=.5):
    # def __init__(self):
        self.myPose=self.mp.solutions.pose.Pose()
    def Marks(self,frame):
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=self.myPose.process(frameRGB)
        poseLandmarks=[]
        if results.pose_landmarks:
            for lm in results.pose_landmarks.landmark:            
                poseLandmarks.append((int(lm.x*width),int(lm.y*height)))
        return poseLandmarks

class mpHands:
    import mediapipe as mp
    def __init__(self,maxHands=2,tol1=1,tol2=.5):
        self.hands=self.mp.solutions.hands.Hands(False,maxHands,tol1,tol2)
    def Marks(self,frame):
        myHands=[]
        handsType=[]
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=self.hands.process(frameRGB)
        if results.multi_hand_landmarks != None:
            #print(results.multi_handedness)
            for hand in results.multi_handedness:
                #print(hand)
                #print(hand.classification)
                #print(hand.classification[0])
                handType=hand.classification[0].label
                handsType.append(handType)
            for handLandMarks in results.multi_hand_landmarks:
                myHand=[]
                for landMark in handLandMarks.landmark:
                    myHand.append((int(landMark.x*width),int(landMark.y*height)))
                myHands.append(myHand)
        return myHands,handsType

width=1200
height=600
cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

findHands=mpHands(2)
findFace=mpFace()
findPose=mpPose()
findMesh=mpFaceMesh(drawMesh=True)

font=cv2.FONT_HERSHEY_SIMPLEX
fontColor=(211,111,222)
fontSize=.1
fontThick=1

cv2.namedWindow('Trackbars')
cv2.moveWindow('Trackbars',width+50,0)
cv2.resizeWindow('Trackbars',400,150)


while True:
    ignore,  frame = cam.read()
    frame=cv2.resize(frame,(width,height))
    handsLM,handsType=findHands.Marks(frame)    #find handtype and handMark
    faceLoc=findFace.Marks(frame)               #find face mark
    poseLM=findPose.Marks(frame)                #find poseture mark
    facesMeshLM=findMesh.Marks(frame,draw=False)           #find face mesh
    if poseLM != []:
        for ind in [13,14,15,16]:
            cv2.circle(frame,poseLM[ind],20,(22,55,77),-1)

    for face in faceLoc:
        cv2.rectangle(frame,face[0],face[1],(212,175,55),3)
    for hand,handType in zip(handsLM,handsType):
        if handType=='Right':
            lbl='Left'
        if handType=='Left':
            lbl='Right'
        cv2.putText(frame,lbl,hand[8],font,2,fontColor,2)
    for faceMeshLM in facesMeshLM:
        cnt=0
        for lm in faceMeshLM:
            cv2.putText(frame,str(cnt),lm,font,fontSize,fontColor,fontThick)
            cnt=cnt+1

    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()








































































# from unittest import result
# import cv2
# print(cv2.__version__)

# class mpFaceMe
# class mpFace:
#     import mediapipe as mp
#     def __init__(self):
#         self.myFace = self.mp.solutions.face_detection.FaceDetection()
#     def Marks(self,frm):
#         frameRGB = cv2.cvtColor(frm,cv2.COLOR_BGR2RGB)
#         result = self.myFace.process(frameRGB)
#         faceBoundBoxs = []
#         if result.detections != None:
#             for face in result.detections:
#                 bBox = face.location_data.relative_bounding_box
#                 topLeft = (int(bBox.xmin*width),int(bBox.ymin*height))
#                 bottomRight = (int((bBox.xmin+bBox.width)*width),int((bBox.ymin+bBox.height)*height))
#                 # print('this is bottom',bottomRight)
#                 # print('bbox.widht',bBox.width)
#                 # print('bbox.height',bBox.height)
#                 faceBoundBoxs.append((topLeft,bottomRight))
#         return faceBoundBoxs    

# class mpPose:
#     import mediapipe as mp
#     def __init__(self,still=False,upperBody = False,smoothData = True):
#         self.myPose = self.mp.solutions.pose.Pose()
#     def Marks(self,frame):
#         frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
#         results = self.myPose.process(frameRGB)
#         landMarkd = []
#         if results.pose_landmarks:
#             for lm in results.pose_landmarks.landmark:
#                 landMarkd.append((int(lm.x*width),int(lm.y*height)))
#         return landMarkd
# class mpHands:
#     import mediapipe as mp
#     def __init__(self,maxHands=2,tol1=1,tol2=.5):
#         self.hands=self.mp.solutions.hands.Hands(False,maxHands,tol1,tol2)
#     def Marks(self,frame):
#         myHands=[]
#         handTpyes = []
#         frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
#         results=self.hands.process(frameRGB)
#         if results.multi_hand_landmarks != None:
#             for thand in results.multi_handedness:
#                 handtype = thand.classification[0].label
#                 handTpyes.append(handtype)
#             for handLandMarks in results.multi_hand_landmarks:
#                 myHand=[]
#                 for landMark in handLandMarks.landmark:
#                     myHand.append((int(landMark.x*width),int(landMark.y*height)))
#                 myHands.append(myHand)
#         return myHands,handTpyes

# width=800
# height=400
# cam=cv2.VideoCapture(0)
# cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
# cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
# cam.set(cv2.CAP_PROP_FPS, 30)
# cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
# handObj = mpHands()
# bodyPos = mpPose()
# facePos = mpFace()
# while True:
#     ignore,  frame = cam.read()
#     frame=cv2.resize(frame,(width,height))
#     handData,handtypes=handObj.Marks(frame)
#     posData = bodyPos.Marks(frame)
#     facexy = facePos.Marks(frame)
#     print(facexy)
#     cv2.circle(frame,posData[5],25,(255,0,255),3)
#     if len(facexy) > 0:
#         cv2.rectangle(frame,facexy[0][0],facexy[0][1],(0,212,200),3)  
#     for hand in handData:
#         for ind in [0,5,6,7,8]:
#             cv2.circle(frame,hand[ind],25,(255,0,255),3)
#     cv2.imshow('my WEBcam', frame)
#     cv2.moveWindow('my WEBcam',0,0)
#     if cv2.waitKey(1) & 0xff ==ord('q'):
#         break
# cam.release()