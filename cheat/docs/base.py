#!/usr/bin/env python
# -*- coding: utf-8 -*-


class BaseDoc(object):

    _doc = {
        "test": "test"
    }

    @classmethod
    def show(cls):
        for doc in cls._doc:
            print("[%s]\n" % doc)
            print("%s\n" % cls._doc[doc])

if __name__ == '__main__':
    BaseDoc.show()
