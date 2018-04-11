#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import logging
import os.path as op


formatStr = '[%(asctime)s] [%(levelname)s] %(message)s'

logger = logging.getLogger("logger")

logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(formatStr)
        
logdir = os.path.join(op.dirname(op.abspath(__file__)), "logs")
logpath = os.path.join(logdir, "%s.log" % time.strftime('%Y-%m-%d', time.localtime(time.time())))
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
