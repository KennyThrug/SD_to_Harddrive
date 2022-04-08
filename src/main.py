import moveFiles
import runGPIO
import os
from time import sleep
def runLoop():
    buttonPressed = False #Quick boolean to make sure holding the button doesn't fuck things up because I know someone would do that :P
    runGPIO.setupButton(24)
    while(True):
        if (buttonPressed == False and runGPIO.checkForButton(24)):
            buttonPressed = True
            print("Find Directory of files")
            sleep(1)
            print("MoveAllFiles") #TODO have each file move a loading bar on the LED
        else:
            if not runGPIO.checkForButton(24):
                buttonPressed = False

if __name__ == '__main__':
    runLoop()


#------098%------
#----Complete----
#--Don't Remove--
#-Safe to Remove-
