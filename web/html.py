#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import chardet


TITLE_REG = re.compile(r'<title>(.*?)</title>')
DESC_REG = re.compile(r'<meta name="description" content="(.*?)">')
KEY_REG = re.compile(r'<meta name="keywords" content="(.*?)">')


def chardecode(string):
    string = string.decode('hex')
    return string.decode(chardet.detect(string)['encoding'])


def contents_handler_reg(contents):
    title = TITLE_REG.findall(contents)
    title = title[0].encode('hex') if len(title) else 'None'

    desc = DESC_REG.findall(contents)
    desc = desc[0].encode('hex') if len(desc) else 'None'

    keywords = KEY_REG.findall(contents)
    keywords = keywords[0].encode('hex') if len(keywords) else 'None'

    if title == keywords == desc == 'None' or (not title):
        return False

    return [title, keywords, desc]


def remove_js_css(content):
    r = re.compile(r'<script.*?</script>', re.I | re.M | re.S)
    s = r.sub('', content)
    r = re.compile(r'<style.*?</style>', re.I | re.M | re.S)
    s = r.sub('', s)
    r = re.compile(r'<!--.*?-->', re.I | re.M | re.S)
    s = r.sub('', s)
    r = re.compile(r'<meta.*?>', re.I | re.M | re.S)
    s = r.sub('', s)
    r = re.compile(r'<ins.*?</ins>', re.I | re.M | re.S)
    s = r.sub('', s)
    return s
