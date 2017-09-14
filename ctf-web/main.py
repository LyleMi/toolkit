#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

from classes.prettytable import PrettyTable
from utils.logger import logger


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
        self.url = url
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
            self.log(r.headers)
        if pContent:
            self.log(r.content)
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
            self.log(r.headers)
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

    def scanlist(self):
        exists = []
        x = PrettyTable()
        x._set_field_names(["Path", "Status", "len"])
        x.align["Path"] = "l"
        with open("./data/pathes.txt") as pathes:
            for p in pathes:
                path = p.strip("\n")
                r = self.get(path)
                x.add_row([path, r.status_code, len(r.content)])
                if r.status_code < 400:
                    exists.append(path)
        print x.get_string()
        self.log("exists")
        self.log(exists)

if __name__ == '__main__':
    c = CTFBase("http://localhost/")
    c.interactive()
