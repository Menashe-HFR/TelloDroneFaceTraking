from djitellopy import tello
import cv2

mendrone = tello.Tello()
mendrone.connect()
print(mendrone.get_battery())

mendrone.streamon()

while True:
    img= mendrone.get_frame_read().frame
    img= cv2.resize(img,(360,240))
    cv2.imshow("image", img)
    cv2.waitKey(1)
