from djitellopy import tello
import KeyPressModule as kp
import time
import cv2

kp.init()
mendrone = tello.Tello()
mendrone.connect()
print(mendrone.get_battery())
global img
mendrone.streamon()

def getKeyboardInput():
    lr, fb, up, yv = 0, 0, 0, 0
    speed = 50
    if kp.getKey("LEFT"): lr = -speed
    elif kp.getKey("RIGHT"): lr = speed

    if kp.getKey("UP"): fb = speed
    elif kp.getKey("DOWN"): fb = -speed

    if kp.getKey("w"): up = speed
    elif kp.getKey("s"): up = -speed

    if kp.getKey("a"): yv = speed
    elif kp.getKey("d"): yv = -speed

    if kp.getKey("q"): mendrone.land(); time.sleep(3)
    if kp.getKey("e"): mendrone.takeoff()

    if kp.getKey("u"): mendrone.flip_forward()
    if kp.getKey("j"): mendrone.flip_back()
    if kp.getKey("k"): mendrone.flip_right()
    if kp.getKey("h"): mendrone.flip_left()


    if kp.getKey('z'):
       cv2.imwrite(f'Resources/Images/{time.time()}.jpg', img)
       time.sleep(0.3)

    if kp.getKey('x'): mendrone.get_video_capture()
    if kp.getKey('c'): mendrone.stop_video_capture()

    return [lr, fb, up, yv]




while True:
    vals = getKeyboardInput()
    mendrone.send_rc_control(vals[0],vals[1],vals[2],vals[3])
    img = mendrone.get_frame_read().frame
    img = cv2.resize(img,(360,240))
    cv2.imshow("image", img)
    cv2.waitKey(1)
