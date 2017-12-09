#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Demo(object):
    __metaclass__ = Singleton

    def __init__(self):
        print "init"

if __name__ == '__main__':
    l = Demo()
    a = Demo()
    print id(l) == id(a)
