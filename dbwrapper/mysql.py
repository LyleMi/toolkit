#!/usr/bin/python
# -*- coding: utf-8 -*-

import pymysql


class DB(object):

    """
    MySQL Database Wrapper
    """

    def __init__(self, opts):
        self.conn = pymysql.connect(
            host=opts["host"],
            user=opts["user"],
            passwd=opts["pwd"],
            db=opts["db"],
            charset='utf8'
        )
        self.cur = self.conn.cursor()

    def showDBs(self):
        self.cur.execute('SHOW DATABASES')
        return [r[0] for r in self.cur.fetchall()]

    def showTables(self):
        self.cur.execute('SHOW TABLES')
        return [r[0] for r in self.cur.fetchall()]

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
        "pwd": "vtu123456",
        "db": "test"
    }
    db = DB(opts)
    print db.showDBs()
    print db.showTables()
    db.insert('1')
    print db.select('1')
