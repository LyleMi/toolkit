#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from docs.linux import linuxDoc
from docs.python import pythonDoc
from docs.ssh import sshDoc
from docs.compress import compressDoc
from docs.iptables import iptablesDoc
from docs.shell import shellDoc

helpDoc = '''
python cheat.py linux
python cheat.py python
python cheat.py ssh
python cheat.py tar
python cheat.py iptables
python cheat.py shell <ip> <port>
'''


def main():
    if len(sys.argv) < 2:
        print("arg plz")
    elif sys.argv[1] == "iptables":
        print(iptablesDoc)
    elif sys.argv[1] == "linux":
        print(linuxDoc)
    elif sys.argv[1] == "python":
        print(pythonDoc)
    elif sys.argv[1] == "ssh":
        print(sshDoc)
    elif sys.argv[1] == "shell":
        shellDoc(sys.argv[2:])
    elif sys.argv[1] == "tar":
        print(compressDoc)
    else:
        print("Keyword not found.")
        print(helpDoc)


if __name__ == '__main__':
    main()
