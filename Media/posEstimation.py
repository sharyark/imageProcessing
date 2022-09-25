import cv2
import mediapipe as mp
print(cv2.__version__)
width = 640
height = 360
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
pos = mp.solutions.pose.Pose()
mpDraw = mp.solutions.drawing_utils
class PosData:
    def __init__(self):
        self.landMarks = []
    def proces(self,x):
        if results.pose_landmarks != None:
            for lm in results.pose_landmarks.landmark:
                self.landMarks.append((int(lm.x*width),int(lm.y*height)))
        return self.landMarks

while True:
    obj = PosData()
    ignore , frame = cam.read()
    frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    print('this is in while')
    results = pos.process(frameRGB)
    data = obj.proces(results)
    print(data)
    cv2.imshow('name1', frame)
    if cv2.waitKey(1) == ord('q'):
        break
cam.release()





















# import cv2
# import mediapipe as mp
# print(cv2.__version__)
# width = 640
# height = 360
# cam = cv2.VideoCapture(0)
# cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
# cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
# pos = mp.solutions.pose.Pose()
# mpDraw = mp.solutions.drawing_utils
# while True:
#     ignore , frame = cam.read()
#     frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
#     print('this is in while')
#     results = pos.process(frameRGB)
#     landMark = []
#     if results.pose_landmarks != None:
#         # mpDraw.draw_landmarks(frame,results.pose_landmarks,mp.solutions.pose.POSE_CONNECTIONS)
#         # print(results)
#         for lm in results.pose_landmarks.landmark:
#             landMark.append((int(lm.x*width),int(lm.y*height)))
#         cv2.circle(frame,landMark[0],20,(112,212,133),5)
#         print(landMark)
#         #     for landmark in handLandMarks.landmark:
#         #         print(landmark.x)
#             # print(handLandMarks.landmark.x,handLandMarks.landmark.y)

#     cv2.imshow('name1', frame)
#     # print(type(results.multi_hand_landmarks))
#     if cv2.waitKey(1) == ord('q'):
#         break
# cam.release()
