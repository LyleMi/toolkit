#!/usr/bin/env python

import zipfile
import os
import optparse
from threading import Thread


def extractFile(z, password):
    try:
        z.extractall(pwd=password)
        print '[+] Found password ' + password + '\n'
    except:
        pass


def main():
    parser = optparse.OptionParser("%prog "+"-f <zipfile>,\
 -d <dictionary>")
    parser.add_option('-f', dest='fname', type='string',
                      help='Your zip file to be cracked')
    parser.add_option('-d', dest='dname', type='string',
                      help='Your dictionary file')
    (options, args) = parser.parse_args()
    if (options.fname == None) | (options.dname == None):
        print parser.usage
        exit(0)
    else:
        zname = options.fname
        dname = options.dname

    zfile = zipfile.ZipFile(zname)
    info = zipfile.ZipInfo(zname)
    info = info.filename
    print '[~] Cracking Password for ' + info + '\n'
    passFile = open(dname)
    for line in passFile.readlines():
        password = line.strip('\n')
        t = Thread(target=extractFile, args=(zfile, password))
        t.start()

if __name__ == '__main__':
    main()
