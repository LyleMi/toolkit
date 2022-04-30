#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docs.base import Base


class Linux(Base):

    _doc = {
        "user": """
# adduser
adduser <username>
useradd -M -N -r -s /bin/bash -c <username>

# change passwd
passwd

# user info
finger <username>

# edit sudoer info
visudo / sudoedit
userdel <username>

# online user
w

# user log
last
lastb # login fail

# group
groupadd
groupdel
groups

# generate password
openssl passwd -6 -salt salt 123456

# add user via edit file
echo 'newuser:x:<UID>:<GID>::/tmp:/bin/sh' | sudo tee -a /etc/passwd
echo 'newuser:x:0:' | sudo tee -a /etc/group
echo 'newuser:$6$salt$MktMKPZJ6t59GfxcJU20DwcwQzfMvOlHFVZiOVD71w.igcOo1R7vBYR65JquIQ/7siC7VRpmteKvZmfSkNc69.:19060:0:99999:7:::' | sudo tee -a /etc/shadow
echo 'newuser:!::' | sudo tee -a /etc/gshadow
echo 'newuser ALL=(ALL:ALL) NOPASSWD: ALL' | sudo tee -a /etc/sudoers
""",
        "process": """
# process status
pidstat 1

pstree [user]

kill <pid>
killall <procname>
pkill <procname>

jobs
fg
bg
""",
        "performance": """
# system load capacity
uptime

# system kernel message
dmesg

# status of memory / cpu / ...
vmstat 1

# cpu time
mpstat -P ALL 1

# io status
iostat -xz 1

# memory
free -m

# net status 
sar -n DEV 1
sar -n TCP,ETCP 1
""",
        "network": """
route -n

# net status 
netstat -tunlp

# network statistics
netstat -s

ss -tunlp
lsof -nP -iTCP -sTCP:LISTEN

# set network bridge
brctl addbr br0
# disable stp
brctl stp br0 off
brctl addif br0 eth0

ethtool

ifconfig
ifconfig <interface> <ip> netmask 255.255.255.0
""",
        "mount": """
[set read-only]
mkdir /mnt/rootvol
rootvol=/mnt/rootvol
sudo mount --bind / $rootvol
sudo mount -o remount,ro $rootvol
""",
        "config": """
# open forward
echo 1 > /proc/sys/net/ipv4/ip_forward
""",
        "tricks": """
# c++ demangling
c++filt

# grep
grep ./ -irnw -e 'search str'

# convert
find . -type f -exec dos2unix {} \\;
""",
        "set coredump": """
# disable core file
ulimit -c 0

# enable core file
ulimit -c unlimited
echo 1 >/proc/sys/kernel/core_uses_pid
echo core > /proc/sys/kernel/core_pattern
echo '/corefiles/core-%e-%p-%t' > /proc/sys/kernel/core_pattern
"""
    }
