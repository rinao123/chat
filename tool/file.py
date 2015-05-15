# -*- coding:utf-8 -*-
import os
import urllib2
import zipfile
import fnmatch

def getAllFilePath(rootPath, patterns="*", isSingleLevel=False, isYieldFloders=False):
    '''遍历目录树，rootPath：根目录，patterns：匹配模式，用分号隔开，如 *.txt;*.doc，
    isSingleLevel=False：遍历子目录，isYieldFloders=False：返回值包括目录'''
    patterns = patterns.split(";")
    for path, subdirs, files in os.walk(rootPath):
        if isYieldFloders:
            files.extend(subdirs)
        files.sort()
        for filename in files:
            for pattern in patterns:
                if fnmatch.fnmatch(filename, pattern):
                    yield os.path.join(path, filename)
                    break
        if isSingleLevel:
                break

def getExtention(filename):
    '''获取文件名的后缀'''
    return os.path.splitext(filename)[1][1:]

def downloadFile(url, savePath, saveFileName):
    '''下载文件'''
    request = urllib2.Request(url)
    downloadFileName = url.split("/")[-1]
    print "正在下载文件%s...." %downloadFileName,
    response = urllib2.urlopen(request).read()
    saveFileName = os.path.join(savePath, saveFileName)
    open(saveFileName, 'wb').write(response)
    print "下载完成"

def unzip_file(zipFileParh, unzipToDir):
    '''解压文件'''
    if not os.path.exists(unzipToDir):
        os.mkdir(unzipToDir, 0777)
    fileName = zipFileParh.split("\\")[-1]
    print "正在解压文件%s...." %fileName,
    zipFileObj = zipfile.ZipFile(zipFileParh)
    for name in zipFileObj.namelist():
        name = name.replace('\\','/')

        if name.endswith('/'):
            os.mkdir(os.path.join(unzipToDir, name))
        else:
            extFileName = os.path.join(unzipToDir, name)
            extDir = os.path.dirname(extFileName)
            if not os.path.exists(extDir):
                os.mkdir(extDir,0777)
            outfile = open(extFileName, 'wb')
            outfile.write(zipFileObj.read(name))
            outfile.close()
    print "解压完成"
