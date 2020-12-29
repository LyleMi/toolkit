#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys
import argparse

from termcolor import colored

import seaborn as sns
import matplotlib.pyplot as plt

from config import Config
from sql import DB
from statistics import Statistics
from utils import highlight
from utils import getValue
from utils import updateValue


def parseArg():
    parser = argparse.ArgumentParser(
        description="cve search",
        usage="[options]"
    )
    parser.add_argument(
        "-i", "--init", action="store_true", help="init database"
    )
    parser.add_argument(
        "-y", "--year", metavar="year", default="", help="year range"
    )
    parser.add_argument(
        "-u", "--update", metavar="update", default="", help="update cve number"
    )
    parser.add_argument(
        "-e", "--exclude", metavar="exclude", default="", help="exclude data"
    )
    parser.add_argument(
        "-s", "--search", metavar="search", default="", help="search data"
    )
    parser.add_argument(
        "-a", "--analyze", metavar="analyze", default="", help="analyze data"
    )
    opts = parser.parse_args()
    """
    if not opts.search and not opts.analyze and not opts.init:
        parser.print_help()
        exit(1)
    """
    return opts


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


def search(keyword, exclude):
    # excludes = exclude.split(",")
    # exclude = exclude.replace(",", "|")
    # print("exclude %s" % exclude)
    keywords = keyword.split(",")
    db = DB(Config.dbOpts)
    sql = 'SELECT `number`, `desc` FROM cve WHERE'
    for key in keywords:
        sql += '`desc` like "%%%s%%" and' % key
    sql = sql[:-4]
    # print(sql)
    ret = db.select(sql)
    for kd in ret:
        # for ex in excludes:
        # print(re.search(exclude, kd[1], re.IGNORECASE))
        if len(exclude) > 0 and re.search(exclude.replace(",", "|"), kd[1], re.IGNORECASE) is not None:
            continue
            # if ex in kd[1]:
        print(colored(kd[0], "yellow"))
        print(highlight(kd[1], keywords))
    print("\ntotal %d results with keywords: %s" % (len(ret), keyword))


def initDB(dbOpts, year):
    minYear = 0
    maxYear = 3000
    year = year.split(",")
    if len(year) == 1:
        minYear = int(year[0])
    elif len(year) == 2:
        minYear = int(year[0])
        maxYear = int(year[1])
    db = DB(dbOpts)
    datas = []
    for kd in getValue(minYear=minYear, maxYear=maxYear):
    # for kd in getValue(minYear=2020, minNumber=4, maxNumber=9):
        # print(kd)
        datas.append(kd)
        if len(datas) > 1000:
            print("insert upto %s" % kd[0])
            db.addCVEData(datas)
            datas = []
    db.addCVEData(datas)


def main():
    opts = parseArg()
    if opts.search:
        search(opts.search, opts.exclude)
    elif opts.analyze:
        statis(opts.analyze)
    elif opts.init:
        initDB(Config.dbOpts, opts.year)
    elif opts.update:
        db = DB(Config.dbOpts)
        datas = [updateValue(opts.update)]
        # print(datas)
        db.addCVEData(datas)
    return


if __name__ == '__main__':
    main()
