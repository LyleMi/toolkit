#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import paramiko


class SSHBatch(object):

    def __init__(self):
        super(SSHBatch, self).__init__()
        self.conns = {}

    def add(self, name, conn, path={}):
        host = conn.get("host")
        port = conn.get("port", 22)
        username = conn.get("username", "root")
        password = conn.get("password", None)
        pkey = conn.get("pkey", None)
        print(f"init {username}@{host}:{port}")
        rsa_key = paramiko.RSAKey.from_private_key_file(pkey)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(
                hostname=host, username=user,
                password=password, pkey=pkey
            )
        except Exception as e:
            print("connection error:", e)
            return False
        self.conns[name] = ssh

    def exectue(self, cmd):
        for name in self.conns:
            client = self.conns[name]
            stdin, stdout, stderr = client.exec_command(cmd)
            print(name, stdout.read())

    def close(self, cmd):
        for name in self.conns:
            self.conns[name].close()


if __name__ == "__main__":
    s = SSHBatch()
    conn = {
        "host": "127.0.0.1",
        "password": "password",
    }
    s.add("test", conn)
    s.exectue("id")
    s.close()
