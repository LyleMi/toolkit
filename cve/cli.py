#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

import seaborn as sns
import matplotlib.pyplot as plt

from config import Config
from sql import DB
from statistics import Statistics
from utils import highlight


def DBStatis(keyword):
    db = DB(Config.dbOpts)
    sql = 'SELECT * FROM cve WHERE `desc` like "%%%s%%"' % keyword
    ret = db.select(sql)
    s = Statistics()
    for kd in ret:
        s.update(kd[1])
        '''
        if 'field' in kd[1]:
            s.update(kd[1])
            # print(kd[0], highlight(kd[1], ['field', keyword]))
        '''
    print(len(ret))
    return s


def statis(keyword):
    s = DBStatis(keyword)
    x = []
    y = []
    for d in s.sortByCount():
        x.append(d[0])
        y.append(d[1])
        print(d[1], d[0])
    # sns.barplot(x=x, y=y)
    # plt.show()
    # s.getCounts(dhcpKey)


def search(keyword):
    db = DB(Config.dbOpts)
    sql = 'SELECT * FROM cve WHERE `desc` like "%%%s%%"' % keyword
    ret = db.select(sql)
    for kd in ret:
        print(kd[0])
        print(highlight(kd[1], keyword))


def main():
    command = sys.argv[1]
    keyword = sys.argv[2]
    if command == 'search':
        search(keyword)
    elif command == 'statis':
        statis(keyword)


if __name__ == '__main__':
    main()
