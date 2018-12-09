#!/bin/sh

# https://github.com/teddysun/shadowsocks_install

wget --no-check-certificate -O shadowsocks-go.sh https://raw.githubusercontent.com/teddysun/shadowsocks_install/master/shadowsocks-go.sh
chmod +x shadowsocks-go.sh
./shadowsocks-go.sh

./shadowsocks-go.sh uninstall
