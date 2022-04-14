import moveFiles
import runGPIO
import FindDirectories
import os
from time import sleep
def runLoop():
    buttonPressed = False #Quick boolean to make sure holding the button doesn't fuck things up because I know someone would do that :P
    runGPIO.setupButton(24)
    while(True):
        if (buttonPressed == False and runGPIO.checkForButton(24)):
            buttonPressed = True
            path = FindDirectories.getBothPaths()
            sleep(1)
            if(path == 1):
                moveFiles.moveFiles("dev2","dev1/Pictures/")
            elif(path == "dev2"):
                moveFiles.moveFiles("dev1","dev2/Pictures/")
            else:
                return
            FindDirectories.unMountDevices()
            runGPIO.writeString("----Complete----\r\n-Safe to Remove-")
            #print("MoveAllFiles") #TODO have each file move a loading bar on the LED
        else:
            if not runGPIO.checkForButton(24):
                buttonPressed = False

if __name__ == '__main__':
    runLoop()


#------098%------
#----Complete----
#--Don't Remove--
#-Safe to Remove-
