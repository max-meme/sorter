from ui_class import UI
from controller_class import Controller
import RPi.GPIO as GPIO

controller = Controller()

#Set GPIO Modes
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(controller.Micros, GPIO.OUT)
GPIO.setup(controller.slp, GPIO.OUT)

controller.set_stepper(False)
interface = UI("hey", controller)