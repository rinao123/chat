# -*- coding:utf-8 -*-
import xlrd
import xlwt
import string

def readExcel(fileName, sheetName):
    '''读取excel表,每一行对应一条记录存入list里，每条记录为一个dictionary，key-标题，value-内容'''
    
    dataList = []
    
    try:
        workbook = xlrd.open_workbook(fileName)
        sheet = workbook.sheet_by_name(sheetName)
    except IOError:
        return dataList
    except xlrd.biffh.XLRDError:
        return dataList
    
    nrows = sheet.nrows
    ncols = sheet.ncols
    for row in range(1, nrows):
        rowDic = {}
        for col in range(ncols):
            key = sheet.cell_value(0, col)
            if not string.isStringLike(key):
                key = str(key)
            value = sheet.cell_value(row, col)
            if not string.isStringLike(value):
                value = str(value)
            rowDic[key] = value
        dataList.append(rowDic)
        
    return dataList

def writeExcel(fileName, sheetName, dataList):
    '''把记录集写入excel表，记录集为list，每一条记录为一个dictionnary，key-标题，value-内容'''
    fileName = string.decodeIfNotUnicode(fileName, "utf-8")
    sheetName = string.decodeIfNotUnicode(sheetName, "utf-8")
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet(sheetName)
    
    index = 0
    row = 1
    titleDic = {}
    for dataDic in dataList:
        for title in dataDic:
            value = dataDic[title]
            title = string.decodeIfNotUnicode(title, "utf-8")
            if title not in titleDic:
                titleDic[title] = index
                sheet.write(0, index, title)
                index += 1
            value = string.decodeIfNotUnicode(value, "utf-8")
            sheet.write(row, titleDic[title], value)
        row += 1
    print titleDic
    
    workbook.save(fileName)
    