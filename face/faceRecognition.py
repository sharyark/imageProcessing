import cv2
import face_recognition as FR
font = cv2.FONT_HERSHEY_SIMPLEX

sharyFace = FR.load_image_file('./abus.png')
faceLoc = FR.face_locations(sharyFace)
knownEncodingsSharyar = FR.face_encodings(sharyFace,faceLoc)
# knownEncodingsSharyar = knownEncodingsSharyar[0]
print(len(knownEncodingsSharyar))

aqibFace = FR.load_image_file('./aqib1.png')
afaceLoc = FR.face_locations(aqibFace)
knownEncodingsAqib = FR.face_encodings(aqibFace,afaceLoc)
# print(len(knownEncodingsAqib))
knownEncodingsAqib = knownEncodingsAqib[0]
bl = FR.compare_faces([knownEncodingsAqib],knownEncodingsSharyar)
print(bl)
# knownEncodings = [knownEncodingsSharyar,knownEncodingsAqib]
# names = ['shayrarKhan','AqibKhan']

# unknownFace = FR.load_image_file('./aqib1.png')
# unknownFaceBGR = cv2.cvtColor(unknownFace,cv2.COLOR_RGB2BGR)
# facelocations = FR.face_locations(unknownFace)
# unknownEncodings = FR.face_encodings(unknownFace,facelocations)
# # print(len(unknownEncodings))
# # cv2.imshow('ch',unknownFace)
# # print('-------------------')
# # print(len(knownEncodings))
# for faceLocation,unknownEncoding in zip(facelocations,unknownEncodings):
#     top,right,bottom,left = faceLocation
#     name = 'unknown person'
#     matches = FR.compare_faces(knownEncodings,unknownEncoding)
#     # print(len(unknownEncoding))
#     print(matches)
#     # if matches:
#     #     cv2.imshow('registered',unknownFaceBGR)
# # objFace = cv2.cvtColor(objFace,cv2.COLOR_RGB2BGR)
# # output = cv2.resize(objFace, (400,600))
# # cv2.imshow('window',output)
# cv2.waitKey(5000)











# # print(faceLoc)
# # top,right,bottom,left = faceLoc
# # cv2.rectangle(objFace,(left,top),(right,bottom),(255,0,0),3)