#!/usr/bin/env python
# -*- coding: utf-8 -*-

import locale
import platform
import re
import subprocess
import sys

ver = sys.version_info
isPY2 = (ver[0] == 2)
isPY3 = (ver[0] == 3)


def getlanguage():
    try:
        language = locale.getdefaultlocale()
    except ValueError:
        language = ('en_US', 'UTF-8')
    return language


def execute(command):
    out, err = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    if isPY3:
        language = getlanguage()
        return (out + err).decode(language[1]).strip()
    return (out + err).strip()


def getSSID(system):
    if system == 'Darwin':
        command = ['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport', '-I']
        pattern = re.compile(r' SSID: (?P<ssid>.+)')
    elif system == 'Linux':
        command = ['nmcli', '-t', '-f', 'active,ssid', 'dev', 'wifi']
        pattern = re.compile(r"yes:'(?P<ssid>.+)'")
    else:
        command = ['netsh', 'wlan', 'show', 'interfaces']
        pattern = re.compile(r' SSID.+: (?P<ssid>.+)\r')
    rs = execute(command)
    match = re.search(pattern, rs)
    if not match:
        return False
    return match.group('ssid')


def GetWifiPassword(ssid, system):
    if system == 'Darwin':
        command = ['security', 'find-generic-password', '-D', 'AirPort network password', '-ga', ssid]
        pattern = re.compile(r'password: "(?P<password>.+)"')
    elif system == 'Linux':
        command = ['sudo', 'cat', '/etc/NetworkManager/system-connections/{0}'.format(ssid)]
        pattern = re.compile(r'psk\=(?P<password>.+)')
    else:
        command = ['netsh', 'wlan', 'show', 'profile', 'name={0}'.format(ssid), 'key=clear']
        language = getlanguage()
        if language[0] == 'zh_CN':
            if isPY3:
                pattern = re.compile(r'关键内容.+: (?P<password>.+)')
            else:
                pattern = re.compile(r'{0}.+: (?P<password>.+)'.format(u'关键内容'.encode(language[1])))
        else:
            pattern = re.compile(r'Key Content.+: (?P<password>.+)')
    rs = execute(command)
    match = re.search(pattern, rs)
    if not match:
        return False
    return match.group('password')


def main():
    system = platform.system()
    if system not in ['Darwin', 'Linux', 'Windows']:
        print('Unknown operation system %s' % (system))
        return
    ssid = getSSID(system)
    if ssid is False:
        print("Get SSID Fail")
        return
    pwd = GetWifiPassword(ssid, system)
    if pwd is False:
        print("Get SSID Fail")
        return
    print("[%s]\n%s" % (ssid, pwd))


if __name__ == '__main__':
    main()
