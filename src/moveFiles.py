import os
def getAllFiles(path):
    listofFiles = []
    for root, dirs, files in os.walk(path):
        for file in files:
            listofFiles.append(os.path.join(root,file))
    return listofFiles
#def moveFiles(folderOne, folderTwo):