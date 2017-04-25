# -*- coding: utf-8 -*-

import socket

host = socket.gethostbyname_ex(socket.gethostname())[2][-1]
port = 9992

if __name__ == '__main__':

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((host, port))
        client.send('A' * 0x1040)
        print 'recv: ', client.recv(4096)
    finally:
        client.close()
        print 'socket closed'
