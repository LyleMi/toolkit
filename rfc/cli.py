#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import requests

def init():
    if not os.path.exists('rfcs'):
        os.mkdir('rfcs')

def main():
    init()
    rfc = sys.argv[1]
    if not rfc.isnumeric():
        return
    s = requests.Session()
    url = "https://tools.ietf.org/rfc/rfc%s.txt" % rfc
    r = s.get(url)
    if r.status_code != 200:
        return
    with open('rfcs/%s.txt' % rfc, 'wb') as fh:
        fh.write(r.content)

if __name__ == '__main__':
    main()
