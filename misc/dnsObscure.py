#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import random
import string
import argparse

from random import randint as ri

import psycopg2
# dnspython
import dns.resolver

# for whole tlds, see https://publicsuffix.org
common_tlds = [
    "com",
    "net",
    "org",
    "top",
    "xyz",
    "cn",
]


def parseArg():
    parser = argparse.ArgumentParser(
        description="try obscure dns query in some unsafe network env",
        usage="[options]",
    )
    parser.add_argument(
        "-t", "--time", type=int, default=-1, help="sleep time"
    )
    opts = parser.parse_args()
    return opts


def debug(msg):
    s = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    print("[%s] %s" % (s, msg))


def crtsh():
    HOST = 'crt.sh'
    NAME = 'certwatch'
    USER = 'guest'
    try:
        conn = psycopg2.connect("dbname=%s user=%s host=%s" % (NAME, USER, HOST))
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute("SELECT NAME_VALUE FROM certificate_identity OFFSET %d LIMIT 10" % ri(1, 0xffff))
    except Exception as e:
        print(repr(e))
        return []
    domains = list(map(lambda i: i[0].lstrip("*."), cursor.fetchall()))
    return domains


def query(domain):
    debug("query domain %s" % domain)
    try:
        dns.resolver.resolve(domain, "A")
    except dns.resolver.NXDOMAIN as e:
        pass


def random_str():
    charset = string.printable[:36]
    length = ri(1, 10)
    return "".join([random.choice(charset) for i in range(length)])


def get_random():
    tld = random.choice(common_tlds)
    d = [random_str() for i in range(ri(1, 3))]
    d.append(tld)
    return ".".join(d)


def chrome_random():
    # see desc here: https://blog.apnic.net/2020/04/13/whats-in-a-name/
    length = ri(7, 15)
    # a-z
    charset = string.printable[10:36]
    return "".join([random.choice(charset) for i in range(length)])


def run_once():
    pick = ri(1, 4)
    if pick == 1:
        domains = crtsh()
        for domain in domains:
            if ri(0, 1):
                query(domain)
            else:
                query(random_str() + "." + domain)
            time.sleep(ri(3, 60))
    elif pick == 2:
        query(get_random())
    elif pick == 3:
        query(chrome_random())


def main():
    opts = parseArg()
    while True:
        run_once()
        if opts.time != -1:
            time.sleep(opts.time)
        else:
            time.sleep(ri(3, 60))


if __name__ == '__main__':
    main()
