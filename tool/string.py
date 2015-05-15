# -*- coding:utf-8 -*-

def isStringLike(obj):
    '''判断一个对象是否类字符串'''
    try:
        obj + ''
        return True
    except:
        return False
    
def decodeIfNotUnicode(obj, code):
    '''把不是unicode的对象转成unicode'''
    if not isStringLike(obj):
        obj = str(obj)
    if not isinstance(obj, unicode):
        obj = obj.decode(code)
    return obj
    