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
"""
    }
