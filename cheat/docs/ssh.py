#!/usr/bin/env python
# -*- coding: utf-8 -*-

sshDoc = """
[Config]

Host name
Hostname x.x.x.x
User root
Port 22
IdentityFile ~/.ssh/keyfile

[SSH Key]

ssh-keygen -t rsa -f keyfilename
scp keyfilename.pub
cat keyfilename .pub >> ~/.ssh/authorized_keys

mkdir ~/.ssh
chmod 700 .ssh
touch authorized_keys
chmod 600 authorized_keys
touch config
chmod 644 config

[Local Forward]

ssh -L <local port>:<remote host>:<remote port> <SSH hostname>

[Remote Forward]

ssh -R <local port>:<remote host>:<remote port> <SSH hostname>
"""
