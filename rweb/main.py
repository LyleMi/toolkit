#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import argparse
import requests

from classes.prettytable import PrettyTable
from utils.domain import parseUrl
from utils.logger import logger
from utils.mprint import printHeader


class CTFBase(object):

    cookie = ""
    proxies = {}
    timeout = 20
    verify = False

    def __init__(self, url=""):
        """
        :param s: store requests session
        :param url: main url
        """
        super(CTFBase, self).__init__()
        self.s = requests.Session()
        self.url = parseUrl(url)
        self.loglevel = "debug"
        self.logger = logger

    def get(self, path, params={}, headers={}, proxies={},
            timeout=None, verify=None, useSession=True,
            pHeader=False, pContent=False):
        if timeout is None:
            timeout = self.timeout
        if verify is None:
            verify = self.verify
        if useSession:
            r = self.s.get(self.url + path, params=params,
                           headers=headers, timeout=timeout,
                           proxies=proxies, verify=verify)
        else:
            r = requests.get(self.url + path, params=params,
                             headers=headers, timeout=timeout,
                             verify=verify)

        if pHeader:
            printHeader(r.headers)
        if pContent:
            print r.content
        return r

    def post(self, path, params={}, data={},
             proxies={}, headers={}, timeout=None,
             verify=None, useSession=True,
             pHeader=False, pContent=False):
        if timeout is None:
            timeout = self.timeout
        if verify is None:
            verify = self.verify
        if useSession:
            r = self.s.post(self.url + path, params=params, data=data,
                            headers=headers, timeout=timeout,
                            proxies=proxies, verify=verify)
        else:
            r = requests.post(self.url + path, params=params, data=data,
                              headers=headers, timeout=timeout,
                              verify=verify)
        if pHeader:
            printHeader(r.headers)
        if pContent:
            self.log(r.content)
        return r

    def interactive(self):
        while True:
            cmd = raw_input(">>> ")
            if cmd in ["exit", "quit"]:
                return
            elif cmd == "set":
                key = raw_input(">>> set what? : ")
                value = raw_input(">>> vaule? : ")
                self.__setattr__(key, value)
                print "set self.%s with value %s" \
                    % (key, self.__getattribute__(key))
                continue
            try:
                call = self.__getattribute__(cmd)
            except AttributeError, e:
                print "has no attribute " + cmd
                continue
            if callable(call):
                call()
            else:
                print call

    def log(self, msg, level=""):
        if level == "":
            level = self.loglevel
        level = level.lower()

        if level == "verbose":
            pass
        elif level == "debug":
            self.logger.debug(msg)
        elif level == "info":
            self.logger.info(msg)
        elif level == "warning":
            self.logger.warning(msg)
        elif level == "error":
            self.logger.error(msg)
        elif level == "critical":
            self.logger.critical(msg)

    def scan(self, ext="php", filename="", interval=0):
        exists = []
        x = PrettyTable()
        x._set_field_names(["Path", "Status", "Len"])
        x.align["Path"] = "l"
        with open("./data/pathes.txt") as pathes:
            for p in pathes:
                path = p.strip("\n")
                if "%ext%" in path:
                    path = path.replace("%ext%", ext)
                elif "%filename%" in path:
                    if not filename:
                        continue
                    path = path.replace("%filename%", filename)
                time.sleep(interval)
                r = self.get(path)
                x.add_row([path, r.status_code, len(r.content)])
                if r.status_code < 400:
                    exists.append(path)
        print x.get_string()
        self.log("exists")
        self.log(exists)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='ctf web intelligent tool',
        usage='%(prog)s [options]',
        epilog='This is a ctf web intelligent tool')
    parser.add_argument('-s', '--scan', action="store_true",
                        help='run with list model')
    parser.add_argument('-f', '--file', metavar='file',
                        default='',
                        help='scan specific file')
    parser.add_argument('-e', '--ext', metavar='ext',
                        default='php',
                        help='scan specific ext')
    parser.add_argument('-i', '--interactive', action="store_true",
                        help='run with interactive model')
    parser.add_argument("-u", '--url',
                        dest="url", help="define specific url")
    parser.add_argument("-t", '--timeinterval', type=int,
                        dest="interval", help="set time interval", default=0)

    opts = parser.parse_args()

    url = opts.url

    if not url:
        sys.stderr.write('Url is required!')
        sys.exit(1)

    c = CTFBase(url)

    if opts.scan:
        c.scan(filename=opts.file,
               interval=opts.interval,
               ext=opts.ext)

    if opts.interactive:
        c.interactive()
