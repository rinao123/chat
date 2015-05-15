# -*- coding:utf-8 -*-

def listGet(l, index, default=None):
    if -len(l) <= index <len(l):
        return index
    else:
        return default
