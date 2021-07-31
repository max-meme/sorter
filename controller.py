from motor_class import Motor
from log import log
import RPi.GPIO as GPIO

#globals
Micros = (23, 24, 25)
Servos = [22, 26, 13, 18]
CW = 1
CCW = 0
SPR = 48 #Stepps per revolution
slp = 14 #Sleep pin
res_multi = 1 #Resolution Multiplier
main_delay = 0.0208 / 128

#motors
#forwards is the direction away from the motors button
motor_x_left = Motor("motor_x_left", 16, 17, 19, CW, CCW)
motor_x_right = Motor("motor_x_right", 4, 5, 20, CW, CCW)
motor_y = Motor("motor_y", 7, 6, 21, CCW, CW)
motor_z = Motor("motor_z", 27, 8, 12, CW, CCW)

motors = [motor_x_left, motor_x_right, motor_y, motor_z]
db = False

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
    log(db, "setting steppers to " + str(status))
    if status:
        GPIO.output(slp, GPIO.HIGH)
    else:
        GPIO.output(slp, GPIO.LOW)

#sets micro stepping resolution
def set_resolution(res):
    log(db, "setting resolution to " + res)
    resolution = {"1": (0, 0, 0),"1/2": (1, 0, 0),"1/4": (0, 1, 0),"1/8": (1, 1, 0),"1/16": (0, 0, 1),"1/32": (1, 0, 1)}
    multiplier = {"1": 1,"1/2": 2,"1/4": 4,"1/8": 8,"1/16": 16,"1/32": 32}
    res_multi = multiplier[res]
    GPIO.output(Micros, resolution[res])


#home all axis
def auto_home(UI):
    print("Auto Home start")
    set_stepper(True)
    set_resolution("1/8")
    home = False
    homing = [[motor_z], [motor_x_left, motor_x_right], [motor_y]]

    #loops trough all motors and checks if their buttons are pressed; stepps if not
    for mots_arr in homing:
        axis_home = False
        while(axis_home == False):
            update_in()
            axis_home = True
            for mot in mots_arr:
                if mot.button == False:
                    axis_home = False
                    mot.make_steps(res_multi, "backwards", main_delay / res_multi / len(mots_arr))
    x = 0
    y = 0
    z = 0
    UI.setxyz(x, y, z)
    UI.addline("> Auto home finished")

def moveto(x_to, y_to, z_to, UI):
    set_stepper(True)
    x_dif = x_to - x
    y_dif = y_to - y
    z_dif = z_to - z

    x_dir = "forwards"
    if x_dif < 0:
        x_dir = "backwards"
    
    y_dir = "forwards"
    if y_dif < 0:
        y_dir = "backwards"
    
    z_dir = "forwards"
    if z_dif < 0:
        z_dir = "backwards"
    
    x_dif_abs = abs(x_dif)
    y_dif_abs = abs(y_dif)
    z_dif_abs = abs(z_dif)

    for i in range(x_dif_abs * res_multi):
        motor_x_left.step(x_dir, main_delay / res_multi / 2)
        motor_x_right.step(x_dir, main_delay / res_multi / 2)
    
    for i in range(y_dif_abs * res_multi):
        motor_y.step(y_dir, main_delay / res_multi)

    for i in range(z_dif_abs * res_multi):
        motor_z.step(z_dir, main_delay / res_multi)
    
    x = x_to
    y = y_to
    z = z_to
    UI.setxyz(x, y, z)
    UI.addline("> move finished")
    
    def moverel(x_rel, y_rel, z_rel):
        moveto(x + x_rel, y + y_rel, z + z_rel)