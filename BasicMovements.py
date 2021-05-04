from djitellopy import tello
from time import sleep

mendrone = tello.Tello()
mendrone.connect()
print("battary : "+mendrone.get_battery()+ "%")

#mendrone.takeoff()
mendrone.flip_forward()
mendrone.send_rc_control(0,50,25,0)
sleep(2)
mendrone.land()
