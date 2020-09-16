#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docs.base import Base


class Chrome(Base):

    _doc = {
        "command line options": """
# disable sandbox
--no-sandbox

# set proxy pac url
--proxy-pac-url

--ignore-certificate-errors
--ignore-urlfetcher-cert-requests

# incognito
--incognito
""",
        "pages": """
chrome://about
chrome://crashes
chrome://history
chrome://net-internals
"""
    }
