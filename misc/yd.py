#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import socket
import string
import httplib2
from bs4 import BeautifulSoup

# 有道词典的API
api = 'http://dict.youdao.com/search?q='


def isChinese(s):
    for i in s:
        if ord(i) >= 19968:
            return True
    return False


def main():
    if len(sys.argv) < 2:
        return
    word = sys.argv[1]
    if len(word) < 1:
        return
    url = api + word
    h = httplib2.Http()
    try:
        headers, content = h.request(url)
    except socket.timeout:
        print("Timeout, dude.")
        return
    if headers.status == 200:
        page = content.decode('utf-8')
    else:
        print("Unable to retrive the page, error code:", headers.status)
        return
    soup = BeautifulSoup(page, "html.parser")
    con = soup.find("div", class_="trans-container")
    if isChinese(word):
        try:
            for i in con.ul.find_all('p'):
                for j in i.find_all('span'):
                    for k in j.find_all('a'):
                        print(k.string)
        except:
            pass
    else:
        try:
            for i in con.ul.find_all('li'):
                print(i.string)
        except AttributeError:
            print("Check your spelling and try again.")
            return

if __name__ == '__main__':
    main()
