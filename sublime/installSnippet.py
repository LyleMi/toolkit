#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
import platform


def main():
    system = platform.system()
    if system == 'Windows':
        sublimeDir = 'D:\\Program Files\\Sublime Text 3\\Data\\Packages\\User\\custom\\'
    elif system == 'Darwin':
        sublimeDir = '~/Library/Application Support/Sublime Text 3/Packages/User/custom/'
        sublimeDir = os.path.expanduser(sublimeDir)
    handleDir(sublimeDir, os.path.abspath('.'))


def handleDir(sublimeDir, dir, prefix=''):
    for filename in os.listdir(dir):
        snippet = os.path.join(dir, filename)
        if snippet.endswith('.sublime-snippet'):
            print('install %s' % snippet)
            shutil.copy(snippet, sublimeDir + prefix + filename)
        elif os.path.isdir(snippet):
            handleDir(sublimeDir, snippet, filename + '-')


if __name__ == '__main__':
    main()
