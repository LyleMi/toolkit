# -*- coding: utf-8 -*-

import socket

target_host = "127.0.0.1"
target_port = 9992

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))

client.send(raw_input('data to be send: '))
response = client.recv(4096)
client.close()
