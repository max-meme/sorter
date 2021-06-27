from motor_class import Motor
from log import log

from time import sleep
import numpy as np
import RPi.GPIO as GPIO

#globals
Micros = (23, 24, 25)
Servos = [22, 26, 13, 18]
CW = 1
CCW = 0
SPR = 48 #Stepps per revolution
slp = 14 #Sleep pin
res_multi = 1 #Resolution Multiplier
main_delay = 0.0208

#motors
#forwards is the direction away from the motors button
motor_x_left = Motor("motor_x_left", 16, 17, 19, CW, CCW)
motor_x_right = Motor("motor_x_right", 4, 5, 20, CW, CCW)
motor_y = Motor("motor_y", 7, 6, 21, CW, CCW)
motor_z = Motor("motor_z", 27, 8, 12, CW, CCW)

motors = [motor_x_left, motor_x_right, motor_y, motor_z]
db = True

x = 0
y = 0
z = 0

x_max = 500
y_max = 500
z_max = 500

# --------functions------

#read motor input pins
def update_in():
    log(db, "reading inputs")
    for mot in motors:
        mot.read_button()
        

#activates and deactivates holding torque
def set_stepper(status):
    log("setting steppers to " + str(status))
    if status:
        GPIO.output(slp, GPIO.HIGH)
    else:
        GPIO.output(slp, GPIO.LOW)

#sets micro stepping resolution
def set_resolution(res):
    log("setting resolution to " + str(res))
    res_multi = res
    resolution = {"1": (0, 0, 0),"1/2": (1, 0, 0),"1/4": (0, 1, 0),"1/8": (1, 1, 0),"1/16": (0, 0, 1),"1/32": (1, 0, 1)}
    GPIO.output(Micros, resolution[str(res)])


#home all axis
def auto_home():
    print(db, "Auto Home start")
    set_stepper(True)
    set_resolution(1/32)
    home = False
    dirs = [CCW, CCW, CCW, CCW]

    #loops trough all motors and checks if their buttons are pressed; stepps if not
    while(home == False):
        home = True
        update_in()
        for mot in motors:
            if mot.button == False:
                home = False
                mot.step("backwards", main_delay * res_multi)


# ------starting code-------

#Set GPIO Modes
GPIO.setmode(GPIO.BCM)
GPIO.setup(Micros, GPIO.OUT)

setOut = [STEPs, DIRs, [slp]]
for i in setOut:
    for y in i:
        GPIO.setup(i, GPIO.OUT)

set_stepper(True)

step_count = SPR * 32

