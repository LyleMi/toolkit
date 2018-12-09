#!/bin/sh

# 3 different server

# https://github.com/Nyr/openvpn-install
wget https://git.io/vpn -O openvpn-install.sh && bash openvpn-install.sh

# https://github.com/angristan/openvpn-install
curl -O https://raw.githubusercontent.com/Angristan/openvpn-install/master/openvpn-install.sh
chmod +x openvpn-install.sh
./openvpn-install.sh

# https://github.com/kylemanna/docker-openvpn
OVPN_DATA="ovpn-data"
docker volume create --name $OVPN_DATA
docker run -v $OVPN_DATA:/etc/openvpn --log-driver=none --rm kylemanna/openvpn ovpn_genconfig -u udp://VPN.SERVERNAME.COM
docker run -v $OVPN_DATA:/etc/openvpn --log-driver=none --rm -it kylemanna/openvpn ovpn_initpki

# client

sudo apt-get install openvpn
# sudo is important 
sudo openvpn --config /path/to/config.ovpn
