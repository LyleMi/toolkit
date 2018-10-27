#!/usr/bin/env python
# -*- coding: utf-8 -*-

iptablesDoc = '''
# list rules

sudo iptables -L

# delete rules by table

sudo iptables -F
sudo iptables -F -t filter
sudo iptables -F -t nat
sudo iptables -F -t mangle

# delete rules by id

iptables -D INPUT 1

# set default

iptables -P INPUT ACCEPT

# addrules 

iptables -I INPUT -p tcp --dport 80 -s 127.0.0.1 -j ACCEPT
iptables -I INPUT -p tcp --dport 80 -j DROP
'''
