#!/usr/bin/python
# -*- coding: utf-8 -*-
"""MySQL Database Wrapper
"""

import pymysql


class DB(object):

    """MySQL Database Wrapper

    Attributes:
        conn (obj): mysql connection
        cur (obj): mysql connection cursor
    """

    def __init__(self, opts):
        """init connection

        Args:
            opts (dict): mysql connection config
        """
        self.conn = pymysql.connect(
            host=opts["host"],
            user=opts["user"],
            passwd=opts["pwd"],
            db=opts["db"],
            charset='utf8'
        )
        self.cur = self.conn.cursor()

    def showDBs(self):
        """show mysql dbs

        Returns:
            dict: databases
        """
        self.cur.execute('SHOW DATABASES')
        return [r[0] for r in self.cur.fetchall()]

    def showTables(self):
        """show mysql tables

        Returns:
            dict: tables
        """
        self.cur.execute('SHOW TABLES')
        return [r[0] for r in self.cur.fetchall()]

    def select(self, sql, data=None):
        """select data

        Args:
            sql (str): sql query
            data (str): condition

        Returns:
            dict: select data
        """
        self.cur.execute(sql, data)
        return self.cur.fetchall()

    def insert(self, sql, data=None, multip=False):
        """insert data

        Args:
            sql (str): sql query
            data (str or list or tuple or dict): data to be insterted
            multip (bool, optional): executemany or one

        Returns:
            int: number of affected rows
        """
        if multip:
            ret = self.cur.executemany(sql, data)
        else:
            ret = self.cur.execute(sql, data)
        self.conn.commit()
        return ret

    def execute(self, sql, data=None):
        """excute raw sql

        Args:
            sql (str): SQL query to be executed
            data (None, optional): parameters used with query
        """
        return self.cur.execute(sql, data)

    def close(self):
        """close connection
        """
        self.cur.close()
        self.conn.close()

    def addCVEData(self, datas):
        sql = "INSERT INTO `cve` (`number`, `name`, `version`, `desc`) VALUES (%s, %s, %s, %s)"
        sql += " ON DUPLICATE KEY UPDATE `name`=VALUES(`name`), `version`=VALUES(`version`), `desc`=VALUES(`desc`)"
        self.insert(sql, datas, True)
