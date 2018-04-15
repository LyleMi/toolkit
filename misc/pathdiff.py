#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import pickle
import sys
import time
import argparse
from hashlib import sha256
from time import sleep

from colorize import colorize


def traverseDir(path, level=0):
    filelist = {}
    for i in os.listdir(path):
        tmp = os.path.join(path, i)
        if os.path.isdir(tmp):
            filelist.update(traverseDir(tmp, level + 1))
        elif os.path.isfile(tmp):
            filelist[tmp] = filesha(tmp)
    return filelist


def filesha(path):
    with open(path, 'rb') as fh:
        return sha256(fh.read()).hexdigest()


def diff(oldlist, newlist):
    for i in oldlist.keys():
        if i not in newlist.keys():
            print(colorize("have been deleted: " + i, 'cyan'))
        elif oldlist[i] == newlist[i]:
            pass
        elif oldlist[i] != newlist[i]:
            print(colorize("changed: " + i, 'green'))
    for i in newlist.keys():
        if i not in oldlist.keys():
            print(colorize("new file: " + i, 'red'))


def main():
    parser = argparse.ArgumentParser(
        description='simple path diff tool',
        usage='%(prog)s [options]',
        epilog='This is a path diff tool')

    parser.add_argument('-i', '--init', action="store_true",
                        help='initial at this path')
    parser.add_argument('-f', '--first', metavar='first',
                        default='',
                        help='first path file to diff')
    parser.add_argument('-s', '--second', metavar='second',
                        default='',
                        help='second path file to diff')
    parser.add_argument('-p', '--persistent', action="store_true",
                        help='run in persistent mode')
    parser.add_argument("-t", '--timesleep', type=int,
                        dest="timesleep", help="set sleeptime", default=10)

    opts = parser.parse_args()

    if (not opts.init) and (not opts.first):
        parser.print_help()
        exit()

    dstDir = os.getcwd()

    if opts.init:
        x = traverseDir(dstDir)
        output = open(time.strftime("%d-%H-%M-%S") + '.pkl', 'wb')
        pickle.dump(x, output)
        output.close()
        return

    pkl_one = open(opts.first, 'rb')
    list_one = pickle.load(pkl_one)
    pkl_one.close()

    if opts.persistent:
        while True:
            try:
                sleep(opts.timesleep)
                x = traverseDir(dstDir)
                diff(list_one, x)
                print("-------------- one round --------------")
            except Exception as e:
                print(e)
                return

    if not opts.second:
        x = traverseDir(dstDir)
        diff(list_one, x)
    else:
        pkl_two = open(opts.second, 'rb')
        list_two = pickle.load(pkl_two)
        diff(list_one, list_two)
        pkl_two.close()


if __name__ == '__main__':
    main()
