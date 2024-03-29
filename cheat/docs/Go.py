#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docs.base import Base


class Go(Base):

    _doc = {
        "proxy": """
export GOPROXY=https://goproxy.io
export GOPROXY=https://goproxy.cn
""",
        "compile": """
go tool compile
""",
        "annotation": """
# disable inline
// go:noinline
""",
    }
