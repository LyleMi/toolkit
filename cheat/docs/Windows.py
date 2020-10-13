#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docs.base import Base


class Windows(Base):

    _doc = {
        "user": """
# adduser
net user /add "<username>" "<password>"
New-LocalUser -Name "<username>" -NoPassword

net user /del "<username>"
""",
        "files": """
# set file attribute
attrib

# 搜索文件
where [/R dir] [/Q] [/F] [/T] pattern

# 获取所有权
takeown

# 修改 ACL
icacls

# bitlocker
manage-bde
manage-bde -lock F:
manage-bde -lock F: -forcedismount
""",
        "process": """
# kill
taskkill.exe /f /im <process_name>
""",
        "services": """
# Services
services.msc

net.exe start <service_name>
net.exe stop <service_name>

sc.exe start <service_name>
sc.exe stop <service_name>
""",
        "cmd": """
# need Consolas font
prompt /?
setx PROMPT ╭─$P$S$_╰─$$$S
setx PROMPT ╭─$S$P$S$C$D$T$H$H$H$F$_╰─$$$S
""",
        "wsl": """
# enable/disable Virtual Machine Platform for wsl2
Enable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform
Disable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
""",
        "vm": """
bcdedit /set hypervisorlaunchtype off
""",
        "misc": """
clip // 定向/重定向到剪贴板
diskmgmt.msc // Disk Management
eventvwr // Event Viewer
gpedit.msc // Group Policy
lusrmgr.msc // Local User / Group
reg // Registry Operation
regedit // Registry Editor
taskmgr // Task Manager

# 启动配置数据存储编辑器
bcdedit

# 控制面板
control

# 创建链接
mklink Link Target
"""
    }
