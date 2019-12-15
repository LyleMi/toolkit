#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import pickle

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Spider(object):

    def __init__(self):
        super(Spider, self).__init__()
        apiUrl = "http://127.0.0.1:4444/wd/hub"
        ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"

        dcc = DesiredCapabilities.CHROME
        dcc['chromeOptions'] = {"args": ["--user-agent=%s" % ua]}

        driver = webdriver.Remote(
            command_executor=apiUrl,
            desired_capabilities=dcc,
        )

    def close(self):
        self.driver.close()

if __name__ == '__main__':
    s = Spider()
