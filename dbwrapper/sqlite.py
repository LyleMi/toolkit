#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3


class DB(object):

    """
    sqlite Database Wrapper
    """

    def __init__(self, database="test.db"):
        super(DB, self).__init__()
        self.conn = sqlite3.connect(database)

    def create(self):
        '''
        create database here
        '''
        cmd = """
        CREATE TABLE `test` (
          `test` varchar(64) NOT NULL
        );
        """
        self.conn.execute(cmd)

    def insert(self, data):
        sql = "INSERT INTO `test` (`test`) VALUES (?)"
        self.conn.execute(sql, [data])
        self.conn.commit()

    def select(self, data):
        sql = "SELECT * FROM test WHERE test = ?"
        cursor = self.conn.execute(sql, [data])
        return [i for i in cursor]

    def interrupt(self):
        '''
        Older SQLite versions had issues with sharing connections between threads. 
        That’s why the Python module disallows sharing connections and cursors between threads. 
        If you still try to do so, you will get an exception at runtime.
        The only exception is calling the interrupt() method, which only makes sense to call from a different thread.
        '''
        self.conn.interrupt()

    def close(self):
        self.conn.close()

if __name__ == '__main__':
    db = DB(":memory:")
    db.create()
    db.insert('1')
    print db.select('1')
    db.interrupt()
    print db.select('1')
    db.close()
