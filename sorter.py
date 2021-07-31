from motor_class import Motor
from log import log
from ui_class import UI
from controller import *
import RPi.GPIO as GPIO

#Set GPIO Modes
GPIO.setmode(GPIO.BCM)
GPIO.setup(Micros, GPIO.OUT)
GPIO.setup(slp, GPIO.OUT)

set_stepper(False)
interface = UI("hey")