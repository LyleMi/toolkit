import socket
import os
import struct
from ctypes import *


def hexdump(src, length=16):
    result = []
    digits = 4 if isinstance(src, str) else 2

    for i in range(0, len(src), length):
        s = src[i:i+length]
        hexa = (' '.join(["%0*X" % (digits, x) for x in s])).encode('ascii')
        text = (''.join([chr(x) if 0x20 <= x < 0x7F else '.' for x in s])).encode('ascii')
        result.append("%04X   %-*s   %s" %
                      (i, length*(digits + 1), hexa, text))

    print('\n'.join(result))


class IP(Structure):
    _fields_ = [
        ("ihl", c_ubyte, 4),
        ("version", c_ubyte, 4),
        ("tos", c_ubyte),
        ("len", c_ushort),
        ("id", c_ushort),
        ("offset", c_ushort),
        ("ttl", c_ubyte),
        ("protocol_num", c_ubyte),
        ("sum", c_ushort),
        ("src", c_ulong),
        ("dst", c_ulong)
    ]

    def __new__(self, socket_buffer=None):
        return self.from_buffer_copy(socket_buffer)

    def __init__(self, socket_buffer=None):
        # map protocol constants to their names
        self.protocol_map = {1: "ICMP", 6: "TCP", 17: "UDP"}
        # human readable IP addresses
        self.src_address = socket.inet_ntoa(struct.pack("<L", self.src))
        self.dst_address = socket.inet_ntoa(struct.pack("<L", self.dst))
        # human readable protocol

        try:
            self.protocol = self.protocol_map[self.protocol_num]
        except:
            self.protocol = str(self.protocol_num)


class ICMP(Structure):
    _fields_ = [
        ("type", c_ubyte),
        ("code", c_ubyte),
        ("checksum", c_ushort),
        ("unused", c_ushort),
        ("next_hop_mtu", c_ushort)
    ]

    def __new__(self, socket_buffer):
        return self.from_buffer_copy(socket_buffer)

    def __init__(self, socket_buffer):
        pass


def main():
    host = socket.gethostbyname_ex(socket.gethostname())[2][-1]

    # create a raw socket and bind it to the public interface
    if os.name == "nt":
        socket_protocol = socket.IPPROTO_IP
    else:
        socket_protocol = socket.IPPROTO_ICMP

    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
    sniffer.bind((host, 0))

    # we want the IP headers included in the capture
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    # if we're using Windows, we need to send an IOCTL
    # to set up promiscuous mode
    if os.name == "nt":
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    try:
        count = 0
        while True:
            # read in a packet
            raw_buffer = sniffer.recvfrom(65565)[0]
            count += 1
            # create an IP header from the first 20 bytes of the buffer
            ip_header = IP(raw_buffer[0:20])
            # print out the protocol that was detected and the hosts
            '''
            print("Protocol: %s\t %s\t -> %s\t" % (ip_header.protocol,
                                                 ip_header.src_address,
                                                 ip_header.dst_address))
            '''

            if ip_header.protocol == "ICMP":
                # calculate where our ICMP packet starts
                offset = ip_header.ihl * 4
                buf = raw_buffer[offset:offset + sizeof(ICMP)]
                # create our ICMP structure
                icmp_header = ICMP(buf)
                print("ICMP -> Type: %d Code: %d" % (icmp_header.type, icmp_header.code))
                print("Src: %s -> Dst: %s" % (ip_header.src_address, ip_header.dst_address))
                hexdump(raw_buffer)

    # handle CTRL-C
    except KeyboardInterrupt:
        # if we're using Windows, turn off promiscuous mode
        if os.name == "nt":
            sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

if __name__ == '__main__':
    main()
