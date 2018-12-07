#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
import sys
import random
import platform
import subprocess

if system == 'Windows':
    import ctypes
    import _winreg as winreg
    WIN_REGISTRY_PATH = "SYSTEM\\CurrentControlSet\\Control\\Class\\{4D36E972-E325-11CE-BFC1-08002BE10318}"

MACRE = re.compile(r"^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$")
system = platform.system()


def isRoot():
    if system == 'Windows':
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    else:
        return os.getuid() == 0


def restartDevice(interface):
    cmd = 'netsh interface set interface "%s" disable' % interface
    subprocess.check_output(cmd)
    cmd = 'netsh interface set interface "%s" enable' % interface
    subprocess.check_output(cmd)


def main():
    if not isRoot():
        print("please run this script as root")
        return
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
        if not MACRE.match(mac):
            print("please use a valid mac address")
            return
    print("change %s's mac to %s" % (interface, mac))
    if system == 'Windows':
        restartDevice(interface)
    elif system == 'Darwin':
        os.system("sudo ifconfig %s ether %s" % (interface, mac))


if __name__ == '__main__':
    main()
