import os
import sys
import re
import shutil

args = sys.argv
projectName = args[1]

fileList = [];

def findFile(dirPath):
    dirs = os.listdir(dirPath)

    for dir in dirs:
        if (dir == ".git"):
            continue
        filePath = dirPath + os.sep + dir

        if (os.path.isfile(filePath)) :
            fileList.append(filePath)
        elif (os.path.isdir(filePath)) :
            findFile(filePath)

findFile(os.getcwd())

for file in fileList :
    splitFileName = os.path.splitext(file)
    if (splitFileName[1] == ".lmpt") :
        f_r = open(file)

        newFileName = splitFileName[0]
        newFileName = newFileName.replace('lampta.conf', projectName + '.conf')
        newFileName = re.sub(re.escape(os.sep + "lampta" + os.sep), re.escape(os.sep + projectName + os.sep), newFileName)

        if not os.path.exists(os.path.dirname(newFileName)) :
            os.makedirs(os.path.dirname(newFileName))
        f_w = open(newFileName, "w")
        fileBody = f_r.read()
        f_w.write(fileBody.replace("<<??>>", projectName))
    else :
        if (os.path.basename(file) == 'lampta.py') :
            continue
        newFileName = re.sub(re.escape(os.sep + "lampta" + os.sep), re.escape(os.sep + projectName + os.sep), file)

        if not os.path.exists(os.path.dirname(newFileName)) :
            os.makedirs(os.path.dirname(newFileName))

        shutil.copy(file, newFileName)