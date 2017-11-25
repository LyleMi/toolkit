#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging

logdir = os.path.join(".", "logs")

logpath = os.path.join(logdir, "log.log")

formatStr = '[%(asctime)s] [%(levelname)s] %(message)s'

logger = logging.getLogger("logger")

logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(formatStr)

if not os.path.exists(logdir):
    os.mkdir(logdir)
fh = logging.FileHandler(logpath)
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)

ch = logging.StreamHandler()
chformatter = logging.Formatter(formatStr)
ch.setLevel(logging.DEBUG)
ch.setFormatter(chformatter)
logger.addHandler(ch)


if __name__ == '__main__':
    logger.debug("test")
