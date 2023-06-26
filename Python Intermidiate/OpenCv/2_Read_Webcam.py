import cv2
 
frameWidth = 2100
frameHeight = 480
cap = cv2.VideoCapture(0) # 0 is use for default camra like laptop camra use  1 for external camra
cap.set(3, frameWidth) #Here 3 is id no: 
cap.set(4, frameHeight)
cap.set(10, 150) # Here this is for brightness
while True:
    success, img = cap.read()
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break