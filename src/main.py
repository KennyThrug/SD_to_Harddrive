import moveFiles
import runGPIO
import os

def runLoop():
    buttonPressed = False #Quick boolean to make sure holding the button doesn't fuck things up because I know someone would do that :P
    runGPIO.setupButton(24)
    while(True):
        if runGPIO.checkForButton(24) and not buttonPressed:
            print("Find Directory of files")
            print("MoveAllFiles") #TODO have each file move a loading bar on the LED
            buttonPressed = True
        else:
            buttonPressed = False

if __name__ == '__main__':
    runLoop()


#------098%------
#----Complete----
#--Don't Remove--
#-Safe to Remove-