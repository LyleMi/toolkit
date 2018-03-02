#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import sqlite3

DBPATH = "ssh.db"  # custom


class DB(object):

    def __init__(self, database="ssh.db"):
        super(DB, self).__init__()
        self.conn = sqlite3.connect(database)
        self.create()

    def create(self):
        sql = '''
        CREATE TABLE IF NOT EXISTS `ssh` (
          `name` varchar(64) NOT NULL,
          `ip` varchar(64) NOT NULL,
          `host` varchar(64) NOT NULL,
          `port` varchar(64) NOT NULL,
          `comment` varchar(100) NOT NULL
        );
        '''
        self.conn.execute(sql)

    def get(self, name):
        sql = "SELECT `ip`, `host`, `port` FROM ssh WHERE name = ?"
        return self.conn.execute(sql, [name]).fetchone()

    def add(self, info):
        name = info[0]
        if self.get(name) is not None:
            print("%s already exist" % sys.argv[2])
            return False
        sql = "INSERT INTO `ssh` (`name`, `ip`, `host`, `port`, `comment`) VALUES (?, ?, ?, ?, ?)"
        ip = info[1]
        host = info[2] if len(info) > 2 else "root"
        port = info[3] if len(info) > 3 else "22"
        comment = " ".join(info[4:])
        self.conn.execute(sql, [name, ip, host, port, comment])
        self.conn.commit()

    def delete(self, name):
        sql = "DELETE FROM `ssh` WHERE name = ?"
        self.conn.execute(sql, [name])
        self.conn.commit()

    def list(self):
        sql = "SELECT `name`, `ip`, `host`, `port`, `comment` FROM ssh"
        return self.conn.execute(sql).fetchall()


def print_help():
    print("python ssh_manager.py list")
    print("python ssh_manager.py con [ssh_name] [command]")
    print("python ssh_manager.py add [ssh_name] [ip] [host] [port] [comment]")
    print("python ssh_manager.py del [ssh_name]")


def main():
    db = DB(DBPATH)
    if len(sys.argv) < 2:
        print_help()
    elif sys.argv[1] == "con":
        info = db.get(sys.argv[2])
        if info is None:
            print("%s not found" % sys.argv[2])
        else:
            cmd = "ssh %s@%s -p %s " % (info[1], info[0], info[2])
            cmd += " ".join(sys.argv[3:])
            os.system(cmd)
    elif sys.argv[1] == "add":
        if db.add(sys.argv[2:]):
            print("Add success")
    elif sys.argv[1] == "del":
        db.delete(sys.argv[2])
    elif sys.argv[1] == "list":
        for i in db.list():
            print("\t".join(i))
    else:
        print_help()


if __name__ == '__main__':
    main()


if __name__ == '__main__':
    if not os.path.exists(DBPATH):
        create_db()
    main()
