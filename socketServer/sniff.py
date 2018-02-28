#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import socket


def main():
    # host to listen on
    host = "0.0.0.0"

    # create a raw socket and bind it to the public interface
    if os.name == "nt":
        socket_protocol = socket.IPPROTO_IP
    else:
        socket_protocol = socket.IPPROTO_TCP

    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)

    sniffer.bind((host, 0))

    # we want the IP headers included in the capture
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    # if we're using Windows, need to send an IOCTL to set up promiscuous mode
    if os.name == "nt":
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    # read in a single packet

    packetNum = 0
    while True:
        data = sniffer.recvfrom(65565)[0]

    # if we're using Windows, turn off promicuous mode
    if os.name == "nt":
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

if __name__ == '__main__':
    main()
