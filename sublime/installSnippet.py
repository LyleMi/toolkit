#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
import platform

def main():
    system = platform.system()
    if system == 'Windows':
        sublimeDir = "D:\\Program Files\\Sublime Text 3\\Data\\Packages\\User\\"
    elif system == 'Darwin':
        sublimeDir = "~/Library/Application Support/Sublime Text 3/Packages/User/"
        sublimeDir = os.path.expanduser(sublimeDir)
    for snippet in os.listdir("."):
        if snippet.endswith(".sublime-snippet"):
            print("install %s" % snippet)
            shutil.copy(snippet, sublimeDir + snippet)

if __name__ == '__main__':
    main()
