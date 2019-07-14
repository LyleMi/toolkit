#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docs.base import Base


class Windows(Base):

    _doc = {
        "Commands": """gpedit.msc // Group Policy
lusrmgr.msc // Local User / Group
services.msc // Services
diskmgmt.msc // Disk Management
regedit // Registry Editor
eventvwr // Event Viewer
taskmgr // Task Manager
"""
    }
