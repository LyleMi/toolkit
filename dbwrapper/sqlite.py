#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3


class DB(object):

    """
    simple sqlite Database wrapper
    """

    def __init__(self, database="test.db"):
        super(DB, self).__init__()
        self.conn = sqlite3.connect(database)

    def create(self):
        cmd = """
        CREATE TABLE `test` (
          `test` varchar(64) NOT NULL
        );
        """
        self.conn.execute(cmd)

    def insert(self, data):
        sql = "INSERT INTO `test` (`test`) VALUES (%s)"
        self.conn.execute(sql % data)
        self.conn.commit()

    def select(self, data):
        sql = "SELECT * FROM test WHERE test = %s"
        cursor = self.conn.execute(sql % data)
        return [i for i in cursor]

if __name__ == '__main__':
    db = DB()
    db.create()
    db.insert('1')
    print db.select('1')
