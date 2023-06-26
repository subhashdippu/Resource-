# This is for Image
# import cv2
# #imread is use to read or  open the image
# image = cv2.imread("/Users/subhashprasad/Documents/New Proj/ImagesAttendance/SubhashPrasad.jpg")
# cv2.imshow("Image ", image) # imshow is use for open and show the image
# cv2.waitKey(0)

# This is for Vedio

import cv2
cap = cv2.VideoCapture("/Users/subhashprasad/Downloads/Radhika Gori Se - Shaadi.mp4") # VideoCapture is use for open video
while True: # We use while loop because cv2 open all the frame of image
    suc, image = cap.read()# suc is use as bool true if video if open then true else false
    cv2.imshow("Video", image)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break