#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import sqlite3

DBPATH = "ssh.db"  # custom


def print_help():
    print("python ssh_manager.py con [ssh_name]")
    print("python ssh_manager.py add [ssh_name] [ip] [host] [port]")
    print("python ssh_manager.py del [ssh_name]")


def create_db():
    conn = sqlite3.connect(DBPATH)
    sql = '''
    CREATE TABLE `ssh` (
      `name` varchar(64) NOT NULL,
      `ip` varchar(64) NOT NULL,
      `host` varchar(64) NOT NULL,
      `port` varchar(64) NOT NULL
    );
    '''
    conn.execute(sql)


def main():
    conn = sqlite3.connect(DBPATH)
    if len(sys.argv) < 3:
        print_help()
    elif sys.argv[1] == "con":
        sql = "SELECT `ip`, `host`, `port` FROM ssh WHERE name = ?"
        cursor = conn.execute(sql, [sys.argv[2]])
        data = [i for i in cursor]
        if len(data) < 1:
            print("%s not found" % sys.argv[2])
        else:
            data = data[0]
            os.system("ssh %s@%s -p %s" % (data[1], data[0], data[2]))
    elif sys.argv[1] == "add":
        sql = "INSERT INTO `ssh` (`name`, `ip`, `host`, `port`) VALUES (?, ?, ?, ?)"
        name = sys.argv[2]
        ip = sys.argv[3]
        if len(sys.argv) > 4:
            host = sys.argv[4]
        else:
            host = "root"
        if len(sys.argv) > 5:
            port = sys.argv[5]
        else:
            port = "22"
        conn.execute(sql, [name, ip, host, port])
        conn.commit()
    elif sys.argv[1] == "del":
        sql = "DELETE FROM `ssh` WHERE name = ?"
        conn.execute(sql, [sys.argv[2]])
        conn.commit()
    else:
        print_help()


if __name__ == '__main__':
    if not os.path.exists(DBPATH):
        create_db()
    main()
