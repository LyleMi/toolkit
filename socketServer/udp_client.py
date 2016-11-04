import socket

host = socket.gethostbyname_ex(socket.gethostname())[2][-1]
port = 19992

if __name__ == '__main__':
    
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client.sendto("AAABBBCCC",(host,port))
        data, addr = client.recvfrom(4096)
        print 'receive data:[%s] from %s:%s' % ((data,) + addr)
    finally:
        client.close()