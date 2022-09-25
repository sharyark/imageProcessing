from email.mime import image
import cv2
from skimage.filters import sobel


img = cv2.imread('./a.jpg')

img1 = cv2.resize(img,(400,300))
# img = cv2.resize(img,(400,300))
imgary = img1[0:90,1:80]
img2 = sobel(img1)

# imgary[:,:] = [255,0,144]
# img1[0:90,1:80] = imgary
# print(imgary)
# changedimg = img1*[0.,0.,1.]
# cv2.imshow('name',img2)
# cv2.imshow('edge',img1)
print('image is ',img1)
print('filtered is ',img2)

cv2.waitKey(0)
cv2.destroyAllWindows()





# [[(1,2,3),(4,5,6),(7,8,9)],
# [(10,11,12),(13,14,15),(16,17,18)],
# [(19,20,21),(22,23,24),(25,26,27)]]