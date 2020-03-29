#!/usr/bin/env python
# -*- coding:utf-8 -*-

import redis


class DB(object):

    def __init__(self, host="localhost"):
        self.r = redis.StrictRedis(
            host=host, port=6379, db=0,
            socket_timeout=timeout
        )
