#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Tool for Debug MicrosoftEdge / IE
Because Edge become an UWP Application in Windows Creator Version
So can't use Windbg debug it with just attach
'''

import os
import sys
import subprocess


def getProgramFiles():
    PFiles = set()
    PFiles.add(os.environ.get('PROGRAMFILES', 'C:\\Program Files'))
    PFiles.add(os.environ.get('PROGRAMFILES(X86)', 'C:\\Program Files(X86)'))
    PFiles.add('C:\\Program Files')
    PFiles.add('C:\\Program Files(X86)')
    tmp = set()
    for r in ["D:", "E:", "F:", "G:"]:
        for p in PFiles:
            tmp.add(p.replace("C:", r))
    return list(tmp.union(PFiles))


def getArch():

    if 'PROCESSOR_ARCHITECTURE' in os.environ:
        arch = os.environ['PROCESSOR_ARCHITECTURE']
    elif 'PROCESSOR_ARCHITEW6432' in os.environ:
        arch = os.environ['PROCESSOR_ARCHITEW6432']
    else:
        arch = "AMD64"
    return "x64" if arch == "AMD64" else "x86"


def getChromeVersion(path=""):
    import re
    version = os.listdir(path)
    version = filter(lambda i: re.match(
        r"^([0-9]{2})(.[0-9]{1,4}){3}$", i), version)
    return sorted(version)[-1]


def getFFVersion(path=""):
    path = os.path.join(path, "application.ini")
    ini = open(path).read().split()
    for i in ini:
        if i.startswith("Version="):
            return i.split("=")[1]
    return None


def getEdgeVersion(xmlpath=""):

    if not xmlpath:
        xmlpath = "C:\\Windows\\SystemApps\\"
        xmlpath += "Microsoft.MicrosoftEdge_8wekyb3d8bbwe\\"
        xmlpath += "AppxManifest.xml"

    if not os.path.exists(xmlpath):
        raise Exception("Edge version not found")

    return open(xmlpath).read().split('Version="')[1].split('"')[0]


def getIEVersion(path=""):
    path = os.path.join(path, "SIGNUP", "install.ins")
    ini = open(path).read().replace("\x00", "").split()
    for i in ini:
        if i.startswith("Version="):
            return i.split("=")[1].replace(",", ".")
    return None


def getWindbPath(arch):

    dbgPath = "%s\\Windows Kits\\%s\\Debuggers\\%s\\WinDbg.exe"

    for winVer in ["10", "8.1", "8.0"]:
        for pf in getProgramFiles():
            path = dbgPath % (pf, winVer, arch)
            if os.path.exists(path):
                return path

    raise Exception("Windbg not found")


def getChromePath():
    path = getProgramFiles()
    path = map(lambda i: os.path.join(
        i, "Google", "Chrome", "Application"), path)
    for p in path:
        if os.path.exists(os.path.join(p, "chrome.exe")):
            return p
    raise Exception("Chrome not found")


def getFFPath():
    path = getProgramFiles()
    path = map(lambda i: os.path.join(i, "Mozilla Firefox"), path)
    for p in path:
        if os.path.exists(os.path.join(p, "firefox.exe")):
            return p
    raise Exception("FireFox not found")


def getIEPath(arch="32"):
    paths = getProgramFiles()
    if arch == "32":
        paths = filter(lambda i: "(x86)" in i, paths)
    elif arch == "64":
        paths = filter(lambda i: "(x86)" not in i, paths)
    for p in paths:
        iepath = os.path.join(p, "Internet Explorer", "iexplore.exe")
        if os.path.isfile(iepath):
            return iepath
    sysdir = "C:\\Windows\\WinSxS"
    for d in os.listdir(sysdir):
        if arch == "32" and d.startswith("amd64"):
            continue
        if arch == "64" and d.startswith("wow64"):
            continue
        iepath = os.path.join(sysdir, d, "iexplore.exe")
        if os.path.isfile(iepath):
            return iepath
    raise Exception("ie not found")


def killProcess(process):
    cmd = "taskkill /f /t /im %s.exe" % process
    os.system(cmd)


def getPid(process):
    p = subprocess.Popen(["tasklist"], stdout=subprocess.PIPE)
    p = p.communicate()[0].split("\r\n")
    pids = []
    for i in p:
        info = i.split()
        if len(info) > 5 and \
                process.lower() + ".exe" == info[0].lower():
            pids.append(info[1])
    return pids

if __name__ == '__main__':

    arch = getArch()
    version = getEdgeVersion()
    windbgPath = getWindbPath(arch)

    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        target = "ie"

    if len(sys.argv) > 2:
        url = sys.argv[2]
    else:
        url = ""

    killProcess("windbg")

    if target.lower() == "edge":
        # packageName = "Microsoft.MicrosoftEdge_%s_neutral__8wekyb3d8bbwe"
        # packageName = packageName % version
        p = subprocess.Popen(["powershell", "-Command", "(Get-AppxPackage Microsoft.MicrosoftEdge).PackageFullName"], stdout=subprocess.PIPE)
        p = p.communicate()[0]
        packageName = p.decode('utf8').split('\n')[0].strip()
        dbgCmd = '"%s" -plmPackage %s -g -plmApp MicrosoftEdge %s'
        dbgCmd = dbgCmd % (windbgPath, packageName, url)
        killProcess("MicrosoftEdge")
        os.system(dbgCmd)
    elif target.lower() == "ie":
        killProcess("iexplore")
        os.system('"%s" %s' % (getIEPath(), url))
        iepid = getPid("iexplore")[-1]
        dbgCmd = '"%s" -p %s -g' % (windbgPath, iepid)
        os.system(dbgCmd)
