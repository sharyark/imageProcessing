import cv2
import face_recognition as FR
font=cv2.FONT_HERSHEY_SIMPLEX
from cmath import pi
from pyfirmata import Arduino , SERVO,util
from time import sleep
import os 

port = '/dev/ttyACM1'
pin = 10
board = Arduino(port)
board.digital[pin].mode = SERVO

def rotateservo(pin,angle):
    board.digital[pin].write(angle)
    sleep(0.015)
rotateservo(pin,50)


imgDirs = ('/home/shary/Desktop/AI/paul/face/demoImages/known')
names = []
knownEncodings = []
for root,dirs,filesz in os.walk(imgDirs):
    for nm in filesz:
        objFace=FR.load_image_file(os.path.join(root,nm))
        faceLoc=FR.face_locations(objFace)
        objEncoded = FR.face_encodings(objFace,faceLoc)
        objEncoded = objEncoded[0]
        knownEncodings.append(objEncoded)
        nm1 = nm.strip('.jpg')
        names.append(nm1)


 
# donFace=FR.load_image_file('demoImages/known/Donald Trump.jpg')
# faceLoc=FR.face_locations(donFace)
# # faceLoc = faceLoc[0]
# donFaceEncode=FR.face_encodings(donFace,faceLoc)
# donFaceEncode = donFaceEncode[0]
 
# nancyFace=FR.load_image_file('demoImages/known/Nancy Pelosi.jpg')
# faceLoc=FR.face_locations(nancyFace)
# nancyFaceEncode=FR.face_encodings(nancyFace,faceLoc)
# nancyFaceEncode = nancyFaceEncode[0]

# penceFace=FR.load_image_file('BB.png')
# faceLoc=FR.face_locations(penceFace)
# penceFaceEncode=FR.face_encodings(penceFace,faceLoc)
# penceFaceEncode = penceFaceEncode[0]


# knownEncodings=[donFaceEncode,nancyFaceEncode,penceFaceEncode]
# names=['Donald Trump','Nancy Pelosi','Sharyar Khan']


cam = cv2.VideoCapture(0) # making camera object
while True:
    ignore , frame = cam.read()
    faceLocations=FR.face_locations(frame)
    unknownEncodings=FR.face_encodings(frame,faceLocations)

    # ignore1 , frame1 = cam.read()
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY )
    # name='Unknown Person'
    if len(unknownEncodings) ==0:
        rotateservo(pin,50)

    for faceLocation,unknownEncoding in zip(faceLocations,unknownEncodings):
        top,right,bottom,left=faceLocation
        # print(faceLocation)
        cv2.rectangle(frame,(left+10,top-10),(right,bottom),(255,0,0),3)
        name='Unknown Person'
        matches=FR.compare_faces(knownEncodings,unknownEncoding)
        # print(matches)
        if True in matches:
            matchIndex=matches.index(True)
            # print(matchIndex)
            # print(names[matchIndex])
            name=names[matchIndex]
        cv2.putText(frame,name,(left,top),font,.75,(0,0,255),2)
        if name == 'Unknown Person':
            # for i in reversed(range(50,160)):
                # if i>=156:
                #     continue
            rotateservo(pin,50)
            print(name)

        else:
            # for i in range(50,160):
                # if i<=156:
                #     continue
            # print(name+'   s')
            rotateservo(pin,160)
    cv2.imshow('My Faces',frame)
   
    # cv2.imshow('name', frame)
    # cv2.imshow('name1', frame1)
    # cv2.imshow('name1', gray)
    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindow()
        # break
cam.release()

