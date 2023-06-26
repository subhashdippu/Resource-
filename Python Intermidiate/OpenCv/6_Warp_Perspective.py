import cv2
import numpy as np
 
img = cv2.imread("/Users/subhashprasad/Documents/New Proj/ImagesAttendance/SubhashPrasad.jpg")

width,height = 250,350
pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]]) # Here four point of image
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]]) # Here  we define four point of image
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))
 
 
cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)
 
cv2.waitKey(0)