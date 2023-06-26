# import cv2
# cam = cv2.VideoCapture(0)
# cam.isOpened()
# while True:

#     ret, frame = cam.read()
#     cv2.imshow('frame',frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cam.release()
# cv2.destroyAllWindows()
import pygame
import pygame.camera
from datetime import datetime
a = datetime.today().strftime("%Y-%m-%d" + " at " + "%I:%M:%S.%f %p")

pygame.camera.init()

camlist = pygame.camera.list_cameras()

if camlist:
    cam = pygame.camera.Camera(camlist[0], (640, 480))
    cam.start()
    image = cam.get_image()
    b = pygame.image.save(image, f"Image {a}.jpg")
    if b == True:
        print("jhjh")
else:
    print("No camera on current device")
