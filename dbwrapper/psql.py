#!/usr/bin/env python
# -*- coding:utf-8 -*-

import psycopg2


class DB(object):

    def __init__(self, opts):
        """init connection

        Args:
            opts (dict): mysql connection config
        """
        dsn = "dbname='%s' user='%s' host='%s' password='%s'"
        dsn = dsn % (opts['db'], opts['user'], opts['host'], opts['pwd'])
        self.conn = psycopg2.connect(dsn)
        self.cur = self.conn.cursor()

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


if __name__ == '__main__':
    pass
