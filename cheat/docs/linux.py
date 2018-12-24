#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import BaseDoc


class linuxDoc(BaseDoc):

    _doc = {
        "add user": "adduser <username>",
        "change passwd": "passwd",
        "c++ demangling": "c++filt",
        "grep": "grep ./ -irnw -e 'search str'",
    }
