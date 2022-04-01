import RPi.GPIO as GPIO
from time import sleep

numGP = 3

def setupLights():
    global numGP
    print(numGP)
    #GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(numGP,GPIO.OUT)
    while(True):
        GPIO.output(numGP,1)
        sleep(1)
        print("on")
        GPIO.output(numGP,0)
        sleep(1)
        print("off")

setupLights()
