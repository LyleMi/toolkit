#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb


class DB(object):

    """
    simple mysql Database wrapper
    """

    def __init__(self, opts):
        self.conn = MySQLdb.connect(
            host=opts["host"],
            user=opts["user"],
            passwd=opts["pwd"],
            db=opts["db"],
            charset='utf8'
        )
        self.cur = self.conn.cursor()

    def insert(self, data):
        sql = "INSERT INTO `test` (`test`) VALUES (%s)"
        self.cur.execute(sql, [data])
        self.conn.commit()

    def select(self, data):
        sql = "SELECT * FROM test WHERE test = %s"
        self.cur.execute(sql, [data])
        # return self.conn.fetchone()
        return self.cur.fetchall()

    def close(self):
        self.cur.close()

if __name__ == '__main__':
    opts = {
        "host": "localhost",
        "user": "root",
        "pwd": "password",
        "db": "db"
    }
    db = DB(opts)
