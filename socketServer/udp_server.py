# -*- coding: utf-8 -*-

import socket
import threading
import traceback

bind_ip = socket.gethostbyname_ex(socket.gethostname())[2][-1]
bind_ip = '127.0.0.1'
bind_port = 19992

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((bind_ip, bind_port))

print "[*] Listening on %s:%d" % (bind_ip, bind_port)
while True:
    try:
        message, address = server.recvfrom(8192)
        print "Got data from", address, ": ", message
        server.sendto(message, address)
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()