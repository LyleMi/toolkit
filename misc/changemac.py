#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import random
import platform

def main():
    if len(sys.argv) < 2:
        print("please choose an interface")
        return
    else:
        interface = sys.argv[1]
    if len(sys.argv) < 3:
        print("choice a random mac")
        mac = ":".join(["%02x" % random.randint(0, 255) for i in range(6)])
    else:
        mac = sys.argv[2]
    print("change %s's mac to %s" % (interface, mac))
    system = platform.system()
    if system == 'Windows':
        pass
    elif system == 'Darwin':
        os.system("sudo ifconfig %s ether %s" % (interface, mac))


if __name__ == '__main__':
    main()
