# -*- coding: utf-8 -*-

import socket
import threading
import traceback

ip = socket.gethostbyname_ex(socket.gethostname())[2][-1]
port = 19992

if __name__ == '__main__':
    
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((ip, port))

    print "[*] Listening on %s:%d" % (ip, port)
    
    while True:
        try:
            message, address = server.recvfrom(8192)
            print "Got data from", address, ": ", message
            server.sendto(message, address)
        except (KeyboardInterrupt, SystemExit):
            exit()
        except:
            traceback.print_exc()