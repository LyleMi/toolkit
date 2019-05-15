#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docs.base import Base


class Linux(Base):

    _doc = {
        "user": """# adduser
adduser <username>
# change passwd
passwd
# user info
finger
# edit sudoer info
visudo / sudoedit

# group
groupadd
groupdel
groups""",
        "performance": """# system load capacity
uptime

# system kernel message
dmesg

# status of memory / cpu / ...
vmstat 1

# cpu time
mpstat -P ALL 1

# process status
pidstat 1

# io status
iostat -xz 1

# memory
free -m

# net status 
sar -n DEV 1
sar -n TCP,ETCP 1""",
        "c++ demangling": "c++filt",
        "grep": "grep ./ -irnw -e 'search str'",
        "open forward": "echo 1 > /proc/sys/net/ipv4/ip_forward",
        "set coredump": """ulimit -c unlimited
echo 1 >/proc/sys/kernel/core_uses_pid
echo '/corefiles/core-%e-%p-%t' > /proc/sys/kernel/core_pattern"""
    }
