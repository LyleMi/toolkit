#!/bin/sh

# https://stackoverflow.com/questions/70963985/error-failed-to-download-metadata-for-repo-appstream-cannot-prepare-internal
sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*

sudo yum update && sudo yum upgrade -y

# add source
sudo yum install -y epel-release

# make tools
sudo yum install -y cmake make clang gcc gcc-c++

# operation tools
sudo yum install -y htop nlod ntop tmux wget curl zsh git gdb

# develop tools
sudo yum install -y git python-pip python-devel openssl-devel

# traffic tools
sudo yum install -y tcpdump tcpflow
sudo yum install -y libpcap-devel

# zsh
sudo yum install -y zsh git
