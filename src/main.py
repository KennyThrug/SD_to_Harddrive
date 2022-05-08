import moveFiles
import runGPIO
import FindDirectories
import os
from time import sleep
def runLoop():
    runGPIO.writeString("Program Ready")
    try:
        buttonPressed = False #Quick boolean to make sure holding the button doesn't fuck things up because I know someone would do that :P
        runGPIO.setupButton(24)
        while(True):
            runGPIO.resetFinalMessage()
            if (buttonPressed == False and runGPIO.checkForButton(24)):
                buttonPressed = True
                path = FindDirectories.getBothPaths()
                sleep(1)
                if(path == 1):
                    moveFiles.moveFiles("dev2","dev1/Pictures/")
                    runGPIO.setFinalMessage("----Complete----\r\n-Safe to Remove-")
                elif(path == 2):
                    moveFiles.moveFiles("dev1","dev2/Pictures/")
                    runGPIO.setFinalMessage("----Complete----\r\n-Safe to Remove-")
                else:
                    runGPIO.setFinalMessage("Please Plug in\r\n Two Seperate Devices")
                FindDirectories.unMountDevices()
                runGPIO.outputFinalMessage()
                #print("MoveAllFiles") #TODO have each file move a loading bar on the LED
            else:
                if not runGPIO.checkForButton(24):
                    buttonPressed = False
    except:
        FindDirectories.unMountDevices()
        runGPIO.outputFinalMessage()
        runLoop()
if __name__ == '__main__':
    runLoop()


#------098%------
#----Complete----
#--Don't Remove--
#-Safe to Remove-
