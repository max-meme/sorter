from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

while True:
    print(GPIO.input(19))
    print(GPIO.input(20))
    print(GPIO.input(21))
    print(GPIO.input(12))
    sleep(1)