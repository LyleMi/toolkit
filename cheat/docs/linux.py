#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import BaseDoc


class linuxDoc(BaseDoc):

    _doc = {
        "add user": "adduser <username>",
        "change passwd": "passwd",
        "c++ demangling": "c++filt",
        "grep": "grep ./ -irnw -e 'search str'",
        "set coredump": """ulimit -c unlimited
echo 1 >/proc/sys/kernel/core_uses_pid
echo '/corefiles/core-%e-%p-%t' > /proc/sys/kernel/core_pattern"""
    }
