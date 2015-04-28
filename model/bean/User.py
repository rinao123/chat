# -*- coding:utf-8 -*-

class User(object):

    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def setUid(self, uid):
        self.uid = uid
        
    def getUid(self):
        return self.uid
    
    def setUsername(self, username):
        self.username = username
    
    def getUsername(self):
        return self.username
    
    def setPassword(self, password):
        self.password = password
    
    def getPassword(self):
        return self.password
        