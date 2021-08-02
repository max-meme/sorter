from motor_class import Motor
from log import log
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

class Controller:
    def __init__(this):
        #globals
        this.Micros = (23, 24, 25)
        this.Servos = [22, 26, 13, 18]
        this.CW = 1
        this.CCW = 0
        this.SPR = 48 #Stepps per revolution
        this.slp = 14 #Sleep pin
        this.res_multi = 1 #Resolution Multiplier
        this.main_delay = 0.0208 / 128

        #motors
        #forwards is the direction away from the this.motors button
        this.motor_x_left = Motor("motor_x_left", 16, 17, 19, this.CW, this.CCW)
        this.motor_x_right = Motor("motor_x_right", 4, 5, 20, this.CW, this.CCW)
        this.motor_y = Motor("motor_y", 7, 6, 21, this.CCW, this.CW)
        this.motor_z = Motor("motor_z", 27, 8, 12, this.CCW, this.CW)

        this.motors = [this.motor_x_left, this.motor_x_right, this.motor_y, this.motor_z]
        this.db = False

        this.x = 0
        this.y = 0
        this.z = 0

        x_max = 500
        y_max = 500
        z_max = 500

    #read motor input pins
    def update_in(this):
        log(this.db, "reading inputs")
        for mot in this.motors:
            mot.read_button()
            

    #activates and deactivates holding torque
    def set_stepper(this, status):
        log(this.db, "setting steppers to " + str(status))
        if status:
            GPIO.output(this.slp, GPIO.HIGH)
        else:
            GPIO.output(this.slp, GPIO.LOW)

    #sets micro stepping resolution
    def set_resolution(this, res):
        log(this.db, "setting resolution to " + res)
        resolution = {"1": (0, 0, 0),"1/2": (1, 0, 0),"1/4": (0, 1, 0),"1/8": (1, 1, 0),"1/16": (0, 0, 1),"1/32": (1, 0, 1)}
        multiplier = {"1": 1,"1/2": 2,"1/4": 4,"1/8": 8,"1/16": 16,"1/32": 32}
        this.res_multi = multiplier[res]
        GPIO.output(this.Micros, resolution[res])


    #home all axis
    def auto_home(this, UI):
        UI.console_addline("Auto Home start")
        UI.ui_set_steppers(True)
        this.set_resolution("1/8")
        home = False
        homing = [[this.motor_z], [this.motor_x_left, this.motor_x_right], [this.motor_y]]

        #loops trough all this.motors and checks if their buttons are pressed; stepps if not
        for mots_arr in homing:
            axis_home = False
            while(axis_home == False):
                this.update_in()
                axis_home = True
                for mot in mots_arr:
                    if mot.button == False:
                        axis_home = False
                        mot.make_steps(this.res_multi, "backwards", this.main_delay / this.res_multi / len(mots_arr))
        this.x = 0
        this.y = 0
        this.z = 0
        UI.setxyz(0, 0, 0)
        UI.console_addline("> Auto home finished")

    def moveto(this, x_to, y_to, z_to, UI):
        UI.ui_set_steppers(True)
        x_dif = x_to - this.x
        y_dif = y_to - this.y
        z_dif = z_to - this.z

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

        for i in range(x_dif_abs * this.res_multi):
            this.motor_x_left.make_steps(this.res_multi, x_dir, this.main_delay / this.res_multi / 2)
            this.motor_x_right.make_steps(this.res_multi, x_dir, this.main_delay / this.res_multi / 2)
        
        for i in range(y_dif_abs * this.res_multi):
            this.motor_y.make_steps(this.res_multi, y_dir, this.main_delay / this.res_multi)

        for i in range(z_dif_abs * this.res_multi):
            this.motor_z.make_steps(this.res_multi, z_dir, this.main_delay / this.res_multi)
        
        this.x = x_to
        this.y = y_to
        this.z = z_to
        UI.setxyz(this.x, this.y, this.z)
        UI.console_addline("> move finished")
        
    def moverel(this, x_rel, y_rel, z_rel, UI):
        this.moveto(this.x + x_rel, this.y + y_rel, this.z + z_rel, UI)