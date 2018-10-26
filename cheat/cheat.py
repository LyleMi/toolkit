#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from docs.linux import linuxDoc
from docs.python import pythonDoc
from docs.ssh import sshDoc

def main():
    if len(sys.argv) < 2:
        print("arg plz")
    elif sys.argv[1] == "linux":
        print(linuxDoc)
    elif sys.argv[1] == "python":
        print(pythonDoc)
    elif sys.argv[1] == "ssh":
        print(sshDoc)
    else:
        print("Keyword not found.")

if __name__ == '__main__':
    main()
