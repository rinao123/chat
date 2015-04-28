# -*- coding:utf-8 -*-
import time

class Chat(object):

    def __init__(self, uid, content):
        self.uid = uid
        self.content = content
        self.time = time.time()
        
    def setCid(self, cid):
        self.cid = cid
        
    def getCid(self):
        return self.cid
    
    def setUid(self, uid):
        self.uid = uid
        
    def getUid(self):
        return self.uid
    
    def setContent(self, content):
        self.content = content
    
    def getContent(self):
        return self.content
        