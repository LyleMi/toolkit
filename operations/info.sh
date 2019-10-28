#!/bin/sh

# os
uname -a
lsb_release -d
cat /etc/os-release
cat /etc/issue

# physical
cat /proc/cpuinfo
cat /proc/meminfo

# user
id
w
last -a

# SELinux
getenforce

# disk
mount
df -h

# program
python --version
perl -v
gcc -v
