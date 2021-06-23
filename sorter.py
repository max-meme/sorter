from time import sleep
import numpy as np
import RPi.GPIO as GPIO


STEPs = [17, 5, 6, 8, 11, 2]
DIRs = [16, 4, 7, 27, 10, 3]
Micros = (23, 24, 25)
CW = 1
CCW = 0
SPR = 48

GPIO.setmode(GPIO.BCM)
GPIO.setup(Micros, GPIO.OUT)

setOut = [STEPs, DIRs]
for i in setOut:
    for y in i:
        GPIO.setup(i, GPIO.OUT)

resolution = {"full": (0, 0, 0),"half": (1, 0, 0),"1/4": (0, 1, 0),"1/8": (1, 1, 0),"1/16": (0, 0, 1),"1/32": (1, 0, 1)}

GPIO.output(Micros, resolution["1/32"])

step_count = SPR * 32
delay = 0.0208 / 32

for x in range(step_count):
    GPIO.output(STEPs[0], GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEPs[0], GPIO.LOW)
    sleep(delay)
