import os
from pickle import NONE
import shutil
from time import localtime, strftime
#import runGPIO

#Takes a path, and gets every file in that folder, recursively.
def getAllFiles(path):
    listofFiles = []
    for root, dirs, files in os.walk(path):
        for file in files:
            listofFiles.append((os.path.join(root,file))[len(path):])
    return listofFiles

#Generates a folder name based off the current time and date
def getFolderName(folderDir):
    curDate = strftime("%Y-%m-%d", localtime())
    curTime = strftime("%H-%M-%S",localtime())
    return folderDir + curDate + "/" + curTime + "/"

#Essentially, takes a file or folder name, and moves it back one directory. Essentially the same thing as doing cd .. in a bash terminal
def moveFileBack(folderName):
    if(folderName == NONE or folderName == ""):
        return ""
    fol = len(folderName)
    back = folderName[::-1]
    for x in back[1:]:
        if(fol == 0):
            return ""
        if(x == '/'):
            print("name: " + folderName[0:fol-1])
            return folderName[0:fol-1]
        else:
            fol = fol-1
        
#Makes the directory that the file is to be put into. If it cannot be made, recursively makes parent folder
def makeDir(folderName):
    if(folderName == None):
        return
    print("Dir:" + folderName)
    try:
        os.mkdir(folderName)
    except:
        makeDir(moveFileBack(folderName))
        try:
            os.mkdir(folderName)
        except:
            print("Got to End of Line")

#Returns True if Drive is able to be unmounted, False otherwise
def unmountDrive(drive):
    print("Todo This")
    return True

#Takes two folders, moves all files from folderOne (RECURSIVELY) to foldertwo
def moveFiles(folderOne, folderTwo):
    folderDest = getFolderName(folderTwo)
    makeDir(folderDest)
    listOfFiles = getAllFiles(folderOne)
    numFiles = len(listOfFiles)
    count = 0
    print("-------0%-------" +
    "\r\n--Don't Remove--")
    for x in listOfFiles:
        makeDir(moveFileBack(folderDest + x))
        shutil.move(folderOne + x,folderDest + x)
        count += 1
        perc = round((count / numFiles) * 100)
        print("-------" + str(perc) + "%------" +
        "\r\n--Don't Remove--")
    print("----Complete----\r\n--Don't Remove--")
    if unmountDrive("hello"):
        print("----Complete----\r\n-Safe to Remove-")
    else:
        print("Error, Cannot\r\n Unmount Drive")
moveFiles('old/','new/')