#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Tool for Debug MicrosoftEdge
Because Edge become an UWP Application in Windows Creator Version
So can't use Windbg debug it with just attach
'''

import os


def getArch():

    if 'PROCESSOR_ARCHITECTURE' in os.environ:
        arch = os.environ['PROCESSOR_ARCHITECTURE']
    elif 'PROCESSOR_ARCHITEW6432' in os.environ:
        arch = os.environ['PROCESSOR_ARCHITEW6432']
    else:
        arch = "AMD64"
    return "x64" if arch == "AMD64" else "x86"


def getVersion(xmlpath=""):

    if not xmlpath:
        xmlpath = "C:\\Windows\\SystemApps\\"
        xmlpath += "Microsoft.MicrosoftEdge_8wekyb3d8bbwe\\"
        xmlpath += "AppxManifest.xml"

    if not os.path.exists(xmlpath):
        raise Exception("Edge version not found")

    return open(xmlpath).read().split('Version="')[1].split('"')[0]


def getWindbPath(arch):

    PFiles = os.environ.get('PROGRAMFILES', 'C:\\Program Files')
    PFilesx86 = os.environ.get('PROGRAMFILES(X86)', 'C:\\Program Files(X86)')

    dbgPath = "%s\\Windows Kits\\%s\\Debuggers\\%s\\WinDbg.exe"

    for winVer in ["10", "8.1", "8.0"]:
        for pf in [PFiles, PFilesx86]:
            path = dbgPath % (pf, winVer, arch)
            if os.path.exists(path):
                return path

    raise Exception("Windbg not found")


def killEdgeProcess():
    cmd = "taskkill /f /t /im MicrosoftEdge.exe"
    os.system(cmd)

if __name__ == '__main__':

    arch = getArch()
    version = getVersion()
    windbgPath = getWindbPath(arch)

    packageName = "Microsoft.MicrosoftEdge_%s_neutral__8wekyb3d8bbwe" % version
    dbgCmd = '"%s" -plmPackage %s -plmApp MicrosoftEdge -g'
    cmd = dbgCmd % (windbgPath, packageName)
    killEdgeProcess()
    os.system(cmd)
