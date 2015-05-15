# -*- coding:utf-8 -*-
import ConfigParser

def getConfig(path, section, key):
    config = ConfigParser.ConfigParser()
    config.read(path)
    if config.has_option(section, key):
        return config.get(section, key)
    else:
        return None
