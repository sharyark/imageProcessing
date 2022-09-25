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
    results = hands.process(frameRGB)
    if results.multi_hand_landmarks != None:
        for handLandMarks in results.multi_hand_landmarks:
            myhand = []
            # # mpDraw.draw_landmarks(frame,handLandMarks,mp.solutions.hands.HAND_CONNECTIONS)
            for landmark in handLandMarks.landmark:
                myhand.append((int(landmark.x*width),int(landmark.y*height)))
            myhands.append(myhand)
    return myhands
# handFunObj = Hand()
while True:
    
    ignore , frame = cam.read()
    handp = handParsing(frame)   #this is using function
    print(len(handp))
    for handone in handp:
        cv2.circle(frame,handone[4],25,(0,123,222),3)
  
    # hand1 = handFunObj.handPoint(frameRGB)
    # print(len(hand1))
    cv2.imshow('name1', frame)
    # print(type(results.multi_hand_landmarks))
    if cv2.waitKey(1) == ord('q'):
        break
cam.release()




    # def __init__(self):
    #     self.hand = mp.solutions.hands.Hands(False,2,1,.5,.5)
    #     self.hand_ = [2,3]
    # def handPoint(self,frm):
    #     self.hand_.clear()
    #     results = self.hand.process(frm)
    #     if results.multi_hand_landmarks != None:
    #         for handLandMarks in results.multi_hand_landmarks:
    #         # # mpDraw.draw_landmarks(frame,handLandMarks,mp.solutions.hands.HAND_CONNECTIONS)
    #             for landmark in handLandMarks.landmark:
    #                 self.hand_.append((int(landmark.x*width),int(landmark.y*height)))
    #     return self.ha