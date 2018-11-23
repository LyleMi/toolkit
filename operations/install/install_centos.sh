#!/bin/sh

sudo yum update && sudo yum upgrade -y

# make tools
sudo yum install -y cmake make clang gcc gcc-c++

# operation tools
sudo yum install -y htop nlod ntop tmux

# develop tools
sudo yum install -y git python-pip python-devel openssl-devel

# traffic tools
sudo yum install -y tcpdump tcpflow
sudo yum install -y libpcap-devel
