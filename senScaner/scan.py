#!/usr/bin/python
# a small scan tool

import sys
import argparse
from time import sleep

import requests

from detect import detect

__author__ = 'sph7'
__DEBUG__ = False
# __DEBUG__ = True


def parseUrl(url):

    if not url.startswith("http://") or url.startswith("https://"):
        if ':443' in url:
            url = "https://" + url
        else:
            url = "http://" + url

    url = (url + '/') if url[-1] != '/' else url

    return url


def main():

    parser = argparse.ArgumentParser(
        description='sensitive path scan tool',
        usage='%(prog)s [options]',
        epilog='This is a sensitive path scan tool')
    parser.add_argument('-l', '--list', action="store_true",
                        help='run with list model')
    parser.add_argument('-f', '--file', metavar='file',
                        default='',
                        help='run with file model')
    parser.add_argument('-p', '--php', action="store_true",
                        help='run with php model')
    parser.add_argument('-d', '--detect', action="store_true",
                        help='run with detect model')
    parser.add_argument('--proxy', metavar='proxy',
                        default='',
                        help='use proxy')
    parser.add_argument("-u", '--url',
                        dest="url", help="use specific url")
    parser.add_argument("-t", '--timeout', type=int,
                        dest="timeout", help="set timeout", default=0)

    opts = parser.parse_args()

    url = opts.url

    if not url:
        parser.print_help()
        sys.stderr.write('Url is required')
        sys.exit(1)

    url = parseUrl(url)

    if not (opts.list or opts.file or opts.php or opts.detect):
        sys.stderr.write('please at least choose a model')
        sys.exit(1)

    timeout = opts.timeout if opts.timeout else 5

    entities = []

    x = ['']

    # print opts

    if opts.list:
        from wordlist import pathlist
        x += pathlist
        # tmp = open("dict/dict.txt", "r")
        # x += [i.strip("\n") for i in tmp]
        # tmp.close()

    # print x

    if opts.file:
        from wordlist import suffixlist
        from wordlist import vimsuffix

        for file in opts.file.split(','):
            x += map(lambda i: file + i, suffixlist)
            x += map(lambda i: '.' + file + i, vimsuffix)

    if opts.php:
        from wordlist import phps
        x += map(lambda i: i + '.php', phps)

    # print x

    headers = {'User-Agent': __import__('wordlist').ua}
    # print headers

    proxies = None

    if opts.proxy:

        proxy = parseUrl(opts.proxy)

        proxies = {
            "http": proxy,
            "https": proxy,
        }

    s = requests.Session()

    for i in x:
        # print i
        sleep(opts.timeout)

        if __DEBUG__:
            continue

        try:
            r = s.get(url+i, headers=headers, timeout=timeout,
                      proxies=proxies, verify=False)
            print(url+i), '\tstatus code: ', r.status_code
            if r.status_code < 400:
                entities.append(i)
        except Exception, e:
            print e

    if opts.detect:
        entities = detect(s, entities, url, headers, timeout, proxies)

    entities = map(lambda i: url + i, entities)
    
    print 'exists:'
    for i in entities:
        print i

if __name__ == '__main__':

    main()

# testcase: python scan.py -l -f index.php,flag.php -t 0 -u localhost
