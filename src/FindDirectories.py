import os

#Takes a path, and gets every file in that folder, recursively.
def getAllFiles(path):
    listofFiles = []
    for root, dirs, files in os.walk(path):
        for file in files:
            listofFiles.append((os.path.join(root,file))[len(path):])
    return listofFiles

def mountAllDevices():
    print("Todo")
def unMountDevices():
    print("Todo")

def checkForHardDrive(path):
    list = getAllFiles(path)
    for x in list:
        print(x)
        if x == "/.HD":
            print("found")
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
            print("ERR: Both dev's\r\nhave .HD file")
        else:
            print("ERR: No dev's\r\nhave .HD file")
    else:
        if(dev1):
            print("dev1 has HD")
        else:
            print("dev2 has HD")
        print("Do moving operation")
    unMountDevices()

if(__name__ == "__main__"):
    getBothPaths()