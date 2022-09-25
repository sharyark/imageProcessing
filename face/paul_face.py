import cv2
import face_recognition as FR
font=cv2.FONT_HERSHEY_SIMPLEX
 
donFace=FR.load_image_file('demoImages/known/Donald Trump.jpg')
faceLoc=FR.face_locations(donFace)
# faceLoc = faceLoc[0]
donFaceEncode=FR.face_encodings(donFace,faceLoc)
donFaceEncode = donFaceEncode[0]
 
nancyFace=FR.load_image_file('demoImages/known/Nancy Pelosi.jpg')
faceLoc=FR.face_locations(nancyFace)
nancyFaceEncode=FR.face_encodings(nancyFace,faceLoc)
nancyFaceEncode = nancyFaceEncode[0]

penceFace=FR.load_image_file('BB.png')
faceLoc=FR.face_locations(penceFace)
penceFaceEncode=FR.face_encodings(penceFace,faceLoc)
penceFaceEncode = penceFaceEncode[0]


# unknownFace=FR.load_image_file('demoImages/unknown/u3.jpg')
# unknownFaceBGR=cv2.cvtColor(unknownFace,cv2.COLOR_RGB2BGR)


knownEncodings=[donFaceEncode,nancyFaceEncode,penceFaceEncode]
names=['Donald Trump','Nancy Pelosi','Sharyar Khan']
cam = cv2.VideoCapture(0) # making camera object
while True:
    ignore , frame = cam.read()
    faceLocations=FR.face_locations(frame)
    unknownEncodings=FR.face_encodings(frame,faceLocations)

    # ignore1 , frame1 = cam.read()
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY )
   
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
    
    cv2.imshow('My Faces',frame)
   
    # cv2.imshow('name', frame)
    # cv2.imshow('name1', frame1)
    # cv2.imshow('name1', gray)
    if cv2.waitKey(1) == ord('q'):
        break
cam.release()



 
 
# cv2.waitKey(10000)


















# for faceLocation,unknownEncoding in zip(faceLocations,unknownEncodings):
#     top,right,bottom,left=faceLocation
#     print(faceLocation)
#     cv2.rectangle(unknownFaceBGR,(left,top),(right,bottom),(255,0,0),3)
#     name='Unknown Person'
#     matches=FR.compare_faces(knownEncodings,unknownEncoding)
#     print(matches)
#     if True in matches:
#         matchIndex=matches.index(True)
#         print(matchIndex)knownEncodings=[donFaceEncode,nancyFaceEncode,penceFaceEncode]
# names=['Donald Trump','Nancy Pelosi','Mike Pence']
 
# unknownFace=FR.load_image_file('C:/Users/Valued Customer/Documents/Python/demoImages/unknown/u1.jpg')
# unknownFaceBGR=cv2.cvtColor(unknownFace,cv2.COLOR_RGB2BGR)
# faceLocations=FR.face_locations(unknownFace)
# unknownEncodings=FR.face_encodings(unknownFace,faceLocations)
 
# for faceLocation,unknownEncoding in zip(faceLocations,unknownEncodings):
#     top,right,bottom,left=faceLocation
#     print(faceLocation)
#     cv2.rectangle(unknownFaceBGR,(left,top),(right,bottom),(255,0,0),3)
#     name='Unknown Person'
#     matches=FR.compare_faces(knownEncodings,unknownEncoding)
#     print(matches)
#     if True in matches:
#         matchIndex=matches.index(True)
#         print(matchIndex)
#         print(names[matchIndex])
#         name=names[matchIndex]
#     cv2.putText(unknownFaceBGR,name,(left,top),font,.75,(0,0,255),2)
 
# cv2.imshow('My Faces',unknownFaceBGR)
 
# cv2.waitKey(10000)
#         print(names[matchIndex])
#         name=names[matchIndex]
#     cv2.putText(unknownFaceBGR,name,(left,top),font,.75,(0,0,255),2)
 
# cv2.imshow('My Faces',unknownFaceBGR)
 
# cv2.waitKey(10000)
# print(len(nancyFaceEncode))

# unknownFace=FR.load_image_file('C:/Users/Valued Customer/Documents/Python/demoImages/unknown/u1.jpg')
# unknownFaceBGR=cv2.cvtColor(unknownFace,cv2.COLOR_RGB2BGR)
# faceLocations=FR.face_locations(unknownFace)
# unknownEncodings=FR.face_encodings(unknownFace,faceLocations)


# penceFace=FR.load_image_file('demoImages/known/Nancy Pelosi.jpg')
# faceLoc=FR.face_locations(penceFace)
# penceFaceEncode=FR.face_encodings(penceFace)
# penceFaceEncode = penceFaceEncode[0]

# bl = FR.compare_faces([nancyFaceEncode],penceFaceEncode)
# print(bl)