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

PFiles = os.environ.get('PROGRAMFILES', 'C:\\Program Files')
PFilesx86 = os.environ.get('PROGRAMFILES(X86)', 'C:\\Program Files(X86)')


def getArch():

    if 'PROCESSOR_ARCHITECTURE' in os.environ:
        arch = os.environ['PROCESSOR_ARCHITECTURE']
    elif 'PROCESSOR_ARCHITEW6432' in os.environ:
        arch = os.environ['PROCESSOR_ARCHITEW6432']
    else:
        arch = "AMD64"
    return "x64" if arch == "AMD64" else "x86"


def getEdgeVer(xmlpath=""):

    if not xmlpath:
        xmlpath = "C:\\Windows\\SystemApps\\"
        xmlpath += "Microsoft.MicrosoftEdge_8wekyb3d8bbwe\\"
        xmlpath += "AppxManifest.xml"

    if not os.path.exists(xmlpath):
        raise Exception("Edge version not found")

    return open(xmlpath).read().split('Version="')[1].split('"')[0]


def getWindbPath(arch):

    dbgPath = "%s\\Windows Kits\\%s\\Debuggers\\%s\\WinDbg.exe"

    for winVer in ["10", "8.1", "8.0"]:
        for pf in [PFiles, PFilesx86]:
            path = dbgPath % (pf, winVer, arch)
            if os.path.exists(path):
                return path

    raise Exception("Windbg not found")


def getIEPath(arch="32"):
    if arch == "32":
        iepath = PFilesx86
    elif arch == "64":
        iepath = PFiles
    iepath = os.path.join(iepath, "Internet Explorer", "iexplore.exe")
    if os.path.exists(iepath):
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
    version = getEdgeVer()
    windbgPath = getWindbPath(arch)

    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        target = "ie"
    
    killProcess("windbg")

    if target.lower() == "edge":
        packageName = "Microsoft.MicrosoftEdge_%s_neutral__8wekyb3d8bbwe" % version
        dbgCmd = '"%s" -plmPackage %s -plmApp MicrosoftEdge -g'
        dbgCmd = dbgCmd % (windbgPath, packageName)
        killProcess("MicrosoftEdge")
        os.system(dbgCmd)
    elif target.lower() == "ie":
        killProcess("iexplore")
        if len(sys.argv) > 2:
            url = sys.argv[2]
        else:
            url = ""
        os.system('"%s" %s' % (getIEPath(), url))
        iepid = getPid("iexplore")[-1]
        dbgCmd = '"%s" -p %s -g' % (windbgPath, iepid)
        os.system(dbgCmd)
