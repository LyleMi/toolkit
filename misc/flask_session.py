#!/usr/bin/env python
# -*- coding: utf-8 -*-

import zlib
from itsdangerous import base64_decode, base64_encode

compressed = False


def decode(cookie):
    global compressed
    payload = cookie
    if payload.startswith('.'):
        compressed = True
        payload = payload[1:]
    data = payload.split(".")[0]
    data = base64_decode(data)
    if compressed:
        data = zlib.decompress(data)
    return data.decode("utf-8")


def encode(cookie):
    global compressed
    if compressed:
        cookie = "." + base64_encode(zlib.compress(cookie))
    else:
        cookie = base64_encode(cookie)
    return cookie
