#!/usr/bin/env python
# -*- coding: utf-8 -*-

sshDoc = """
Config

    Host name
    Hostname x.x.x.x
    User root
    Port 22
    IdentityFile ~/.ssh/keyfile

SSH Key

    ssh-keygen -t rsa -C joyqi -f keyfilename
    scp keyfilename.pub 
    cat keyfilename .pub >> ~/.ssh/authorized_keys

Local Forward

    ssh -L <local port>:<remote host>:<remote port> <SSH hostname>

Remote Forward

    ssh -R <local port>:<remote host>:<remote port> <SSH hostname>
"""
