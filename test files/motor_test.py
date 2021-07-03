import RPi.GPIO as GPIO
from time import sleep

stp_pin = 6
dir_pin = 7
Micros = (23, 24, 25)
delay = 0.0208 / 32

GPIO.setmode(GPIO.BCM)
GPIO.setup(Micros, GPIO.OUT)
GPIO.setup(stp_pin, GPIO.OUT)
GPIO.setup(dir_pin, GPIO.OUT)

resolution = {"1": (0, 0, 0),"1/2": (1, 0, 0),"1/4": (0, 1, 0),"1/8": (1, 1, 0),"1/16": (0, 0, 1),"1/32": (1, 0, 1)}
GPIO.output(Micros, resolution["1/32"])

while True:
    GPIO.output(stp_pin, GPIO.HIGH)
    sleep(delay)
    GPIO.output(stp_pin, GPIO.LOW)
    sleep(delay)
