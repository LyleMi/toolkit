#!/bin/sh

# server
# https://github.com/teddysun/shadowsocks_install

wget --no-check-certificate -O shadowsocks-go.sh https://raw.githubusercontent.com/teddysun/shadowsocks_install/master/shadowsocks-go.sh
chmod +x shadowsocks-go.sh
./shadowsocks-go.sh

./shadowsocks-go.sh uninstall

# client
sudo pip install shadowsocks
echo '{
    "server": "1.1.1.1",
    "server_port": 8388,
    "local_address": "127.0.0.1",
    "local_port": 1080,
    "password": "passwd",
    "timeout": 300,
    "method": "aes-256-cfb"
}' >> ~/ss.json
sslocal -c ~/ss.json

sudo apt install -y proxychains
sudo vi /etc/proxychains.conf
sudo echo 'socks5 127.0.0.1 1080' >> /etc/proxychains.conf
