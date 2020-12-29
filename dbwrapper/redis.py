#!/usr/bin/env python
# -*- coding:utf-8 -*-

import redis


class DB(object):

    def __init__(self, host="localhost", timeout=5):
        self.r = redis.StrictRedis(
            host=host, port=6379, db=0,
            socket_timeout=timeout
        )

    def get(self, key):
        return self.r.get(key)

    def set(self, key, value):
        return self.r.set(key, value)
