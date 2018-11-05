#!/usr/bin/env python
# -*- coding: utf-8 -*-

iptablesDoc = '''
# save rules

service iptables save

# list rules

iptables -n -v -L --line-numbers

## list all active rules

iptables -S

# delete rules by table

iptables -F
iptables -F -t filter
iptables -F -t nat
iptables -F -t mangle

# delete rules by table and number

iptables -D INPUT 1

# set default

iptables -P INPUT ACCEPT

# addrules 

## allow

### ip and port

iptables -I INPUT -p tcp --dport 80 -s 127.0.0.1 -j ACCEPT

### connect status

iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

## block

iptables -I INPUT -p tcp --dport 80 -j DROP
'''
