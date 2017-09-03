#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

from utils.logger import logger
from utils.common import randua


class CTFBase(object):

    url = ""
    cookie = ""

    def __init__(self):
        super(CTFBase, self).__init__()
        self.s = requests.Session()
        self.defaultlevel = "debug"
        self.logger = logger

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
            level = self.defaultlevel

        if level == "debug":
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
