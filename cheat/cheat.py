#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from docs.linux import linuxDoc
from docs.python import pythonDoc
from docs.ssh import sshDoc
from docs.compress import CompressDoc
from docs.iptables import iptablesDoc
from docs.shell import shellDoc
from docs.mysql import MySQLDoc
from docs.git import GitDoc

helpDoc = '''
python cheat.py linux
python cheat.py python
python cheat.py ssh
python cheat.py tar
python cheat.py iptables
python cheat.py mysql
python cheat.py git
python cheat.py shell <ip> <port>
'''


def main():
    if len(sys.argv) < 2:
        print("arg plz")
    elif sys.argv[1] == "iptables":
        iptablesDoc.show(sys.argv[2:])
    elif sys.argv[1] == "linux":
        linuxDoc.show(sys.argv[2:])
    elif sys.argv[1] == "python":
        pythonDoc.show(sys.argv[2:])
    elif sys.argv[1] == "ssh":
        sshDoc.show(sys.argv[2:])
    elif sys.argv[1] == "shell":
        shellDoc(sys.argv[2:])
    elif sys.argv[1] == "tar":
        CompressDoc.show(sys.argv[2:])
    elif sys.argv[1] == "mysql":
        MySQLDoc.show(sys.argv[2:])
    elif sys.argv[1] == "git":
        GitDoc.show(sys.argv[2:])
    else:
        print("Keyword not found.")
        print(helpDoc)


if __name__ == '__main__':
    main()
