# -*- coding: utf-8 -*-

import os
import pickle
import sys
import time
import argparse
from hashlib import sha256

from colorize import colorize

filelist = {}


class PathTree(object):

    """docstring for PathTree"""

    def __init__(self, path, level=0, debug=False):
        self.path = path
        self.level = level
        self.debug = debug
        self.childpath = []

        # print retract + 'init path:', path

        for i in os.listdir(path):

            tmp = os.path.join(path, i)

            self.retractPrint(i)

            if os.path.isdir(tmp):
                self.childpath.append(PathTree(tmp, level + 1))
            elif os.path.isfile(tmp):
                filelist[tmp] = filesha(tmp)

    def retractPrint(self, s):
        if self.debug:
            print self.level * '  ', s


def filesha(path):
    tmp = open(path, 'r')
    s = sha256(tmp.read()).hexdigest()
    tmp.close()
    return s


def diff(oldlist, newlist):

    for i in oldlist.keys():

        if i not in newlist.keys():
            print colorize("have been deleted: " + i, 'cyan')
        elif oldlist[i] == newlist[i]:
            pass
        elif oldlist[i] != newlist[i]:
            print colorize("changed: " + i, 'green')

    for i in newlist.keys():
        if i not in oldlist.keys():
            print colorize("new file: " + i, 'red')


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

    opts = parser.parse_args()

    if (not opts.init) and (not opts.first):
        parser.print_help()
        exit()

    if opts.init:
        x = PathTree(os.getcwd())
        output = open(time.strftime("%d-%H-%M-%S") + '.pkl', 'wb')
        pickle.dump(filelist, output)
        output.close()
    else:
        pkl_one = open(opts.first, 'rb')
        list_one = pickle.load(pkl_one)

        if not opts.second:
           x = PathTree(os.getcwd())
           diff(list_one, filelist)
        else:
            pkl_two = open(opts.second, 'rb')
            list_two = pickle.load(pkl_two)
            diff(list_one, list_two)
            pkl_two.close()
        pkl_one.close()

if __name__ == '__main__':
    main()
