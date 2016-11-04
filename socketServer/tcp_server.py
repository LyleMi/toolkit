# -*- coding: utf-8 -*-

import socket
import threading

ip = socket.gethostbyname_ex(socket.gethostname())[2][-1]
port = 9992


def handle_client(client_socket):
    try:
        request = client_socket.recv(1024)
        print "[*] Received: %s" % request
        client_socket.send("ACK!")
    finally:
        client_socket.close()
        print "[*] Conection closed."

if __name__ == '__main__':

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))

    server.listen(5)
    print "[*] Listening on %s:%d" % (ip, port)

    while True:
        
        client, addr = server.accept()
        print "[*] Accepted connection from: %s:%d" % (addr[0], addr[1])
        # spin up our client thread to handle incoming data
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()
