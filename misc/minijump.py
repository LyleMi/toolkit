#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
import os.path as op

base = op.dirname(op.abspath(__file__))
table = op.join(base, 'jumptable.json')
jbat = op.join(base, 'j.bat')

def load():
    if not op.exists(table):
        return {}
    with open(table, 'r') as fh:
        return json.load(fh)


def save(jumptable):
    with open(table, 'w') as fh:
        json.dump(jumptable, fh)


def add(short, fullpath):
    jumptable = load()
    jumptable[short] = fullpath
    print('add shortcut %s for %s success' % (short, fullpath))
    save(jumptable)
    gen()


def delete(short):
    jumptable = load()
    del jumptable[short]
    save(jumptable)
    print('delete shortcut %s success' % short)
    gen()


def listtable():
    jumptable = load()
    keys = list(jumptable.keys())
    keys.sort()
    mlen = max([len(i) for i in keys])
    for key in keys:
        print(key.ljust(mlen + 4, ' '), jumptable[key])


def gen():
    jumptable = load()

    fileContent = """@echo off

if "%1" == "a" goto add
if "%1" == "d" goto delete
if "%1" == "g" goto gen
if "%1" == "l" goto list
"""

    for i in jumptable:
        fileContent += 'if "%1" == "' + i + '" goto ' + i + '\n'

    fileContent += '\n'
    fileContent += """
:add
py "%~dp0\\j.py" %1 %2 %3
goto end

:delete
py "%~dp0\\j.py" %1 %2
goto end

:gen
py "%~dp0\\j.py" %1
goto end

:list
py "%~dp0\\j.py" %1
goto end
"""

    for i in jumptable:
        fileContent += ':%s\n' % i
        fileContent += jumptable[i].split('\\')[0] + '\n'
        fileContent += 'cd %s\n' % jumptable[i]
        fileContent += 'goto end\n\n'

    fileContent += '\n'
    fileContent += ':end\n'

    f = open(jbat, 'w')
    f.write(fileContent)
    f.close()


if __name__ == '__main__':
    if sys.argv[1] == 'a':
        add(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == 'd':
        delete(sys.argv[2])
    elif sys.argv[1] == 'l':
        listtable()
    elif sys.argv[1] == 'g':
        gen()
    else:
        print('j a short fullpath')
        print('j d short')
        print('j l')
        print('j g')
