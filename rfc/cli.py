#!/usr/bin/env python
# -*- coding: utf-8 -*-
# to sync all rfcs, use
# rsync -avz rsync.tools.ietf.org::tools.id ./id


import os
import sys
import requests


def init():
    if not os.path.exists('rfcs'):
        os.mkdir('rfcs')


def search():
    rfcdir = ""
    keyword = b""
    for file in os.listdir(rfcdir):
        filepath = os.path.join(rfcdir, file)
        if not filepath.endswith(".txt"):
            continue
        with open(filepath, "rb") as fh:
            content = fh.read()
            if keyword in content:
                print(file)


def main():
    init()
    rfc = sys.argv[1]
    targets = []
    if rfc.isnumeric():
        targets.append(rfc)
    elif "-" in rfc:
        lower, upper = map(int, rfc.split("-"))
        targets = [i for i in range(lower, upper + 1)]
    if len(targets) < 1:
        return
    s = requests.Session()
    for rfc in targets:
        getOne(rfc)


def getOne(rfc, update=False):
    filepath = os.path.join('rfcs', '%s.txt' % rfc)
    if os.path.exists(filepath) and not update:
        return
    url = "https://tools.ietf.org/rfc/rfc%s.txt" % rfc
    r = s.get(url)
    if r.status_code != 200:
        return
    with open('rfcs/%s.txt' % rfc, 'wb') as fh:
        fh.write(r.content)


if __name__ == '__main__':
    main()
