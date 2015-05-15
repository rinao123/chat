# -*- coding:utf-8 -*-
from tool import file

'''遍历根目录指定类型的文件，查找包括关键字的行'''

def printPathAndLine(filePath, line):
    print filePath, line

def findTheLine(filePath, keyword, doSomething=printPathAndLine):
    theFile = open(filePath)
    for line in theFile:
        if keyword in line:
            doSomething(filePath, line)

def main():
    filePathList = list(file.getAllFilePath(ur"E:\wxrpg\newwxrpg\common\私服\xmldata\activity", patterns="*.xml"))
    for filePath in filePathList:
        findTheLine(filePath, "alwaysShowEffectUrl")

if __name__ == '__main__':
    main()
