#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

import seaborn as sns
import matplotlib.pyplot as plt

from config import Config
from sql import DB
from statistics import Statistics
from utils import highlight

def searchDB(keyword):
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


if __name__ == '__main__':
    product_name = 'Microsoft Edge'
    product_name = 'Safari'
    product_name = 'Firefox'
    product_name = 'Chrome'
    year = '2018'
    keyword = 'DHCP'
    keyword = sys.argv[1]
    s = searchDB(keyword)
    x = []
    y = []
    for d in s.sortByCount():
        x.append(d[0])
        y.append(d[1])
        print(d[1], d[0])
    # sns.barplot(x=x, y=y)
    # plt.show()
    # s.getCounts(dhcpKey)
