import os
import sys

xmlpath = "C:\\Windows\\SystemApps\\"
xmlpath += "Microsoft.MicrosoftEdge_8wekyb3d8bbwe\\AppxManifest.xml"

if not os.path.exists(xmlpath):
    print "xml file not found. exit!"
    exit()

version = open(xmlpath).read().split('Version="')[1].split('"')[0]

windbgpath = ""

if 'PROCESSOR_ARCHITECTURE' in os.environ:
    arch = os.environ['PROCESSOR_ARCHITECTURE']
elif 'PROCESSOR_ARCHITEW6432' in os.environ:
    arch = os.environ['PROCESSOR_ARCHITEW6432']
else:
    arch = "AMD64"

if arch == "AMD64":
    osisa = "x64"
else:
    osisa = "x86"

if 'PROGRAMFILES' in os.environ:
    ProgramFiles = os.environ['PROGRAMFILES']
else:
    ProgramFiles = 'C:\\Program Files'

if 'PROGRAMFILES' in os.environ:
    ProgramFilesx86 = os.environ['PROGRAMFILES(X86)']
else:
    ProgramFiles = 'C:\\Program Files(X86)'


if not windbgpath:
    windbgpath = "%s\\Windows Kits\\10\\Debuggers\\%s\\WinDbg.exe" % (
        ProgramFiles, osisa)
    if not os.path.exists(windbgpath):
        windbgpath = ""

if not windbgpath:
    windbgpath = "%s\\Windows Kits\\10\\Debuggers\\%s\\WinDbg.exe" % (
        ProgramFilesx86, osisa)
    if not os.path.exists(windbgpath):
        windbgpath = ""

if not windbgpath:
    print "windbg not found. exit!"
    exit()

packagename = "Microsoft.MicrosoftEdge_%s_neutral__8wekyb3d8bbwe" % version
cmd = '"%s" -plmPackage %s -plmApp MicrosoftEdge -g' % (
    windbgpath, packagename)
os.system(cmd)
