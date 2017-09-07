#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

from utils.logger import logger
from utils.common import randua


class CTFBase(object):

    url = ""
    cookie = ""
    proxies = {}
    timeout = 20
    verify = False

    def __init__(self):
        """
        :param s: store requests session
        """
        super(CTFBase, self).__init__()
        self.s = requests.Session()
        self.loglevel = "debug"
        self.logger = logger
        self.ua = randua()

    def cookieHeader(self, headers={}, cookie=""):
        headers["Cookie"] = cookie if cookie else self.cookie
        return headers

    def jsonHeader(self, headers={}):
        headers["Content-type"] = "application/json"
        return headers

    def uaHeader(self, headers={}, UA=""):
        headers["User-Agent"] = UA if UA else randua()
        return headers

    def setUrl(self):
        self.url = raw_input("Input url: ")

    def setCookie(self):
        self.cookie = raw_input("Input cookie: ")

    def setUa(self):
        self.ua = raw_input("Input UA: ")

    def get(self, url, params={}, headers={},
            timeout=self.timeout, verify=self.verify):
        r = self.s.get(url, params=params,
                       headers=headers, timeout=timeout,
                       verify=verify)
        self.log(r.content, "verbose")
        return r

    def post(self, url, params={}, data=data,
             headers={}, timeout=self.timeout,
             verify=self.verify):
        r = self.s.post(url, params=params, data=data,
                        headers=headers, timeout=timeout,
                        verify=verify)
        self.log(r.content, "verbose")
        return r

    def interactive(self):
        while True:
            cmd = raw_input(">>> ")
            if cmd in ["exit", "quit"]:
                return
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

if __name__ == '__main__':
    c = CTFBase()
    c.interactive()
