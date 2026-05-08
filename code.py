# Code for HW3

from gpiozero import Button, MotionSensor
from picamera2 import Picamera2 
from time import sleep
from signal import pause
import sys 
import os

# create objects that refer to a button,
# a motion sensor and the Picamera2
button = Button(2)
pir = MotionSensor(4)
camera = Picamera2() 

config = camera.create_still_configuration()
camera.configure(config)
camera.start()

# image image names
i = 0

# stop the camera when the pushbutton is pressed
def stop_camera():
    camera.stop()
    # exit the program
    os._exit(0)

# take photo when motion is detected
def take_photo():
    global i
    i = i + 1
    camera.capture_file('/home/pi/Desktop/image_%s.jpg' % i)
    print('A photo has been taken')
    sleep(3)

# assign a function that runs when the button is pressed
button.when_pressed = stop_camera

# assign a function that runs when motion is detected
pir.when_motion = take_photo

pause()
