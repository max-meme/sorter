import RPi.GPIO as GPIO
from time import sleep
from log import log
GPIO.setwarnings(False)

db = False

class Motor:
    def __init__(this, name, dir_pin, step_pin, button_pin, forwards, backwards):
        log(db, "Creating Motor " + name)

        this.name = name
        this.dir_pin = dir_pin
        this.step_pin = step_pin
        this.button_pin = button_pin
        this.button = False
        this.backwards = backwards
        this.forwards = forwards

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(dir_pin, GPIO.OUT)
        GPIO.setup(step_pin, GPIO.OUT)
        GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def make_steps(this, steps, in_direction, delay):
        log(db, this.name + " is making Step " + in_direction)

        direction = 0
        if in_direction == "forwards":
            direction = this.forwards
        elif in_direction == "backwards":
            direction = this.backwards
        GPIO.output(this.dir_pin, direction) #set direction; can be 1 or 0
        for i in range(steps):
            GPIO.output(this.step_pin, GPIO.HIGH)
            sleep(delay)
            GPIO.output(this.step_pin, GPIO.LOW)
            sleep(delay)

    def read_button(this):
        log(db, "reading inputs")
        status = GPIO.input(this.button_pin)
        if status == 1:
            this.button = False
        else:
            this.button = True
        log(db, str(this.button) + ": " + str(status))
