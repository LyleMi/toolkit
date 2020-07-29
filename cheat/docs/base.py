#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Base(object):

    _doc = {
        "test": "test"
    }

    cmdhelp = "[keyword]"

    @classmethod
    def show(cls, keys=False):
        if keys and keys[0] == "keys":
            for k in cls._doc.keys():
                print(k)
            return
        for doc in cls._doc:
            if keys and doc not in keys and len(keys) != 1:
                continue
            if len(keys) == 1 and keys[0] not in doc:
                continue
            print("[%s]\n" % doc)
            print("%s\n" % cls._doc[doc].lstrip("\n").rstrip("\n"))

if __name__ == '__main__':
    BaseDoc.show()
