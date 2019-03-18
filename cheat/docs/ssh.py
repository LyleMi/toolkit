#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .base import BaseDoc


class sshDoc(BaseDoc):

    _doc = {
        "config": """Host name
Hostname x.x.x.x
User root
Port 22
IdentityFile ~/.ssh/keyfile
""",
        "key": """ssh-keygen -t rsa -f keyfilename
scp keyfilename.pub
cat keyfilename .pub >> ~/.ssh/authorized_keys

mkdir ~/.ssh
chmod 700 ~/.ssh
touch ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
touch ~/.ssh/config
chmod 644 ~/.ssh/config""",
        "local forward": """ssh -L <local port>:<remote host>:<remote port> <SSH hostname>""",
        "remote forward": """ssh -R <local port>:<remote host>:<remote port> <SSH hostname>"""
    }
