#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
import sys
import random
import argparse
import platform
import subprocess

system = platform.system()

if system == 'Windows':
    import ctypes
    try:
        import winreg
    except ImportError:
        import _winreg as winreg
    WIN_REGISTRY_PATH = "SYSTEM\\CurrentControlSet\\Control\\Class\\{4D36E972-E325-11CE-BFC1-08002BE10318}"

MACRE = re.compile(r"^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$")


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

    parser = argparse.ArgumentParser(
        description='Tool For Change Mac Address',
        usage='[options]')
    parser.add_argument('-m', '--mac', metavar='mac',
                        default='',
                        help='mac address')
    parser.add_argument('-i', '--interface', metavar='interface',
                        default='',
                        help='network interface')
    parser.add_argument('-d', '--desc', metavar='desc',
                        default='',
                        help='network interface desc')
    opts = parser.parse_args()
    if not opts.interface:
        parser.print_help()
        print("please choose an interface")
        return
    interface = opts.interface
    desc = opts.desc
    mac = opts.mac
    if not mac or not MACRE.match(mac):
        print("choice a random mac")
        mac = ":".join(["%02x" % random.randint(0, 255) for i in range(6)])
    print("change %s's mac to %s" % (interface, mac))
    if system == 'Windows':
        reg_hdl = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
        key = winreg.OpenKey(reg_hdl, WIN_REGISTRY_PATH)
        info = winreg.QueryInfoKey(key)

        adapter_key = None
        adapter_path = None

        for x in range(info[0]):
            subkey = winreg.EnumKey(key, x)
            path = WIN_REGISTRY_PATH + "\\" + subkey

            if subkey == 'Properties':
                break

            # Check for adapter match for appropriate interface
            new_key = winreg.OpenKey(reg_hdl, path)
            try:
                adapterDesc = winreg.QueryValueEx(new_key, "DriverDesc")
                if adapterDesc[0] == desc:
                    adapter_path = path
                    break
                else:
                    winreg.CloseKey(new_key)
            except WindowsError as err:
                if err.errno == 2:  # register value not found, ok to ignore
                    pass
                else:
                    raise err

        if adapter_path is None:
            print('get adapter path fail')
            winreg.CloseKey(key)
            winreg.CloseKey(reg_hdl)
            return
        else:
            print(f'adapter_path {adapter_path}')
        adapter_key = winreg.OpenKey(reg_hdl, adapter_path, 0, winreg.KEY_WRITE)
        winreg.SetValueEx(adapter_key, "NetworkAddress", 0, winreg.REG_SZ, mac)
        winreg.CloseKey(adapter_key)
        winreg.CloseKey(key)
        winreg.CloseKey(reg_hdl)
        restartDevice(interface)
    elif system == 'Darwin':
        os.system("sudo ifconfig %s ether %s" % (interface, mac))


if __name__ == '__main__':
    main()
