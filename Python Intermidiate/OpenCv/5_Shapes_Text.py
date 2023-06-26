import cv2
import numpy as np
 
img = np.zeros((512,512,3),np.uint8)# here we create a matrix with numpy size 512 and here the 3 is chennel name which means color. np.uint8 this will give the value from 0 to 255
#print(img)
#img[:]= 255,0,0
 
# Here first argument is image, second is first and second cordinates 
# Third is color 0,255,0 this is green 
# fourth is thikness 3
cv2.line(img,(0,0),(300,300),(0,255,0),3) 
# img.shape[1] width, img.shape[0] heigh
# cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(255,0,0),2) 

cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)
cv2.circle(img,(400,50),30,(255,255,0),5)
# word start from (300,200)
# font name FONT_HERSHEY_COMPLEX
# Here 1 after the font size of text
# Here 3 after the color thickness
cv2.putText(img," OPENCV  ",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),3)
 
 
cv2.imshow("Image",img)
 
cv2.waitKey(0)