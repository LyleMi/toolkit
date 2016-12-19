# -*- coding: utf-8 -*-

import os
import pickle
from hashlib import sha256

filelist = {}

class PathTree(object):
    
    """docstring for PathTree"""

    def __init__(self, path, level = 0, debug = False):
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
            print i, "have been deleted"
        elif oldlist[i] == newlist[i]:
            pass
        elif oldlist[i] != newlist[i]:
            print i, "changed"

    for i in newlist.keys():
        if i not in oldlist.keys():
            print "new file", i

if __name__ == '__main__':
    x = PathTree(os.getcwd())
    pkl_file = open('data.pkl', 'rb')
    # output = open('data.pkl', 'wb')
    # pickle.dump(filelist, output)
    oldlist = pickle.load(pkl_file)
    diff(oldlist, filelist)
    pkl_file.close()
    # output.close()