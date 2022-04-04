import os
import shutil
from time import localtime, strftime

def getAllFiles(path):
    listofFiles = []
    for root, dirs, files in os.walk(path):
        for file in files:
            listofFiles.append(os.path.join(root,file))
    return listofFiles
def getFolderName(folderDir):
    curDate = strftime("%Y-%m-%d", localtime())
    curTime = strftime("%H-%M-%S",localtime())
    return folderDir + curDate + "/" + curTime + "/"

def moveFileBack(folderName):
    fol = len(folderName)
    back = folderName[::-1]
    for x in folderName[1:]:
        if(fol == 0):
            return ""
        if(x == '/'):
            print("name: " + folderName[0:fol-1])
            return folderName[0:fol-1]
        else:
            fol = fol-1
        

def makeDir(folderName):
    try:
        os.mkdir(folderName)
    except:
        makeDir(moveFileBack(folderName))
        os.mkdir(folderName)

def moveFiles(folderOne, folderTwo):
    folderDest = getFolderName(folderTwo)
    makeDir(folderDest)
    listOfFiles = getAllFiles(folderOne)
    print(folderDest)
    print(listOfFiles)
    for x in listOfFiles:
        print("")
        makeDir(moveFileBack(folderDest + x))


#shutil.move('old/EmptyFile', 'new/test_file.txt')
#print(getAllFiles("old/"))
#moveFiles("old/","new/")
moveFiles("old/","new/")