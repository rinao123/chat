# -*- coding:utf-8 -*-

import MySQLdb

class MysqlToool(object):

    def __init__(self, host, port, database, username, password="", charset="utf-8"):
        self.connection = MySQLdb.connect(host=host, port=port, db=database, user=username, passwd=password, charset=charset)

    def __del__(self):
        self.connection.close()

    def query(self, sql):
        pass

