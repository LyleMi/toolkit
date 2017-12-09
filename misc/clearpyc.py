#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os


def traverseDir(path, level=0):
    for i in os.listdir(path):
        tmp = os.path.join(path, i)
        if os.path.isdir(tmp):
            traverseDir(tmp, level + 1)
        elif os.path.isfile(tmp):
            if tmp.endswith(".pyc"):
                os.remove(tmp)


def main():
    x = traverseDir(os.getcwd())


if __name__ == '__main__':
    main()
