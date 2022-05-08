import os
import runGPIO

#Takes a path, and gets every file in that folder, recursively.
def getAllFiles(path):
    listofFiles = []
    for root, dirs, files in os.walk(path):
        for file in files:
            listofFiles.append((os.path.join(root,file))[len(path):])
    return listofFiles

#Takes a path, and gets every file in that folder, but doesn't search farther than initial directory
def getFirstFiles(path):
    return os.listdir(path)

listOfDevices = "abcdefghijklmnopqrstuvwxyz"

def mountAllDevices():
    try:
        os.mkdir("dev1")
        os.mkdir("dev2")
    except:
        runGPIO.writeString("Todo")
    isDone = False
    isHalf = False
    for i in listOfDevices:
        if(isHalf == False):
            if(os.system("sudo mount /dev/sd" + i + "1 dev1") == ""):
                isHalf = True
        elif(isDone == False):
            if(os.system("sudo mount /dev/sd" + i + "1 dev2") == ""):
                isDone = True
                break
def unMountDevices():
    try:
        os.system("sudo umount dev1")
        runGPIO.writeString("device success\r\n unmounted")
    except:
        runGPIO.writeString("ERR: device not unmounted")
    try:
        os.system("sudo umount dev2")
        runGPIO.writeString("device success\r\n unmounted")
    except:
        runGPIO.writeString("ERR: device2\r\n not unmounted")
    runGPIO.writeString("Todo")

def checkForHardDrive(path):
    list = getFirstFiles(path)
    for x in list:
        if x == '.HD':
            runGPIO.writeString("found")
            return True
    return False

def getBothPaths():
    mountAllDevices()

    #Check to see which device is the Hardrive and which is the SD card
    #HD will have a .HD File on the root directory
    #If neither of them do, throw an error
    dev1 = checkForHardDrive("dev1")
    dev2 =  checkForHardDrive("dev2")
    if(dev1 == dev2):
        if(dev1):
            runGPIO.writeString("ERR: Both dev's\r\nhave .HD file")
        else:
            runGPIO.writeString("ERR: No dev's\r\nhave .HD file")
    else:
        if(dev1):
            runGPIO.writeString("dev1 has HD")
            return 1
        else:
            runGPIO.writeString("dev2 has HD")
            return 2
    return 0

#if(__name__ == "__main__"):
#    getBothPaths()
