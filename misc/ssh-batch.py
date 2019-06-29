#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import paramiko


def exectue(host, user, password, cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(
            hostname=host, username=user, password=password
        )
    except Exception as e:
        print("connection error:", e)
        return False

    stdin, stdout, stderr = ssh.exec_command(cmd)
    print(stdout.read())
    ssh.close()
    return True


if __name__ == "__main__":
    exectue('127.0.1.1', 'root', 'password', 'uname -a')
