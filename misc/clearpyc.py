#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import shutil
from pathlib import Path


class DirTraverser(object):

    """traverse Dir with callback"""

    def __init__(self, callback):
        super(DirTraverser, self).__init__()
        self.callback = callback

    def traverse(self, path, level=0):
        for p in path.iterdir():
            if p.is_dir():
                self.traverse(p, level + 1)
                self.callback(p, 'dir')
            elif p.is_file():
                self.callback(p, 'file')


def clearpyc(path, ftype):
    if ftype == 'dir':
        if path.name == "__pycache__":
            shutil.rmtree(path)
    elif ftype == 'file':
        if path.suffix == ".pyc":
            path.unlink()


def js2ts(path, ftype):
    if ftype == 'file' and path.suffix == '.js':
        ts = str(path)[:-2] + 'ts'
        path.rename(ts)


def main():
    d = DirTraverser(clearpyc)
    p = Path()
    if len(sys.argv) > 1:
        p = Path(sys.argv[1])
    else:
        p = Path()
        p = p.resolve()
    d.traverse(p)


if __name__ == '__main__':
    main()
