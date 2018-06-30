#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


def main():
    if len(sys.argv) < 2:
        return

    filename = sys.argv[1]

    dicts = {
        ".tar.gz": "tar zxvf",
        ".tar": "tar xvf",
        ".gz": "gunzip",
        ".tar.bz2": "tar jxvf",
        ".tar.bz": "tar jxvf",
        ".bz2": "bunzip2",
        ".tar.Z": "tar Zxvf",
        ".Z": "uncompress",
    }

    prefix = ""

    for i in dicts:
        if filename.endswith(i):
            prefix = dicts[i]
            break

    if not prefix:
        return

    os.system(prefix + " " + filename)


if __name__ == '__main__':
    main()
