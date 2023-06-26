import cv2
import numpy as np
 
img = cv2.imread("/Users/subhashprasad/Documents/New Proj/ImagesAttendance/SubhashPrasad.jpg")
print(img.shape)
 
imgResize = cv2.resize(img,(1000,500))
print(imgResize.shape)
 
imgCropped = img[0:3000,200:7000] # here crop though codinates
 
cv2.imshow("Image",img)
#cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Cropped",imgCropped)
 
cv2.waitKey(0)