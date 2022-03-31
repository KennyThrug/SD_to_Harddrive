import RPi.GPIO as GPIO
from time import sleep

def setupLights():
    GPIO.setwarnings(False)
    GPIO.setMode(GPIO.BOARD)
    GPIO.setup(8,GPIO.OUT,initial=GPIO.LOW)

def blinkLights(numSeconds):
    while True:
        GPIO.output(8,GPIO.HIGH)
        sleep(1)
        GPIO.output(8,GPIO.LOW)
        sleep(1)