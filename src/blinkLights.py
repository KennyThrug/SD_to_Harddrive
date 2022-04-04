from pickle import TRUE
import RPi.GPIO as GPIO
from time import sleep

def blinkLights(numGP,numButton):
    print(numGP)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(numGP,GPIO.OUT)

    GPIO.setup(numButton,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

    while(True):
        if GPIO.input(numButton) == GPIO.HIGH:
            for x in range(4):
                 GPIO.output(numGP,1)
                 sleep(1)
                 print("on")
                 GPIO.output(numGP,0)
                 sleep(1)
                 print("off")
        else:
            GPIO.output(numGP,0)
        
