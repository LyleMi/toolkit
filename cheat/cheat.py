#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import imp


def init():
    base = os.path.dirname(os.path.abspath(__file__))
    docs = os.path.join(base, 'docs')
    skip = ['__init__.py', 'base.py', '__pycache__']
    entries = {}
    for filename in os.listdir(docs):
        if filename in skip:
            continue
        key = filename.split('.')[0]
        module = imp.load_source(key, os.path.join(docs, filename))
        entries[key.lower()] = getattr(module, key)
    return entries


def main():
    entries = init()
    if len(sys.argv) < 2:
        print("arg plz")
    elif sys.argv[1] in entries:
        entries[sys.argv[1]].show(sys.argv[2:])
    else:
        print("Keyword not found.")
        for key in entries:
            print('python cheat.py %s %s' % (key, entries[key].cmdhelp))


if __name__ == '__main__':
    main()
