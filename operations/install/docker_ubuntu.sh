#!/bin/sh

# https://docs.docker.com/install/linux/docker-ce/ubuntu/
curl -sSL https://get.docker.com/ | sudo sh

sudo apt remove docker docker-engine docker.io

# for ubuntu 14.x
sudo apt install -y linux-image-extra-$(uname -r) linux-image-extra-virtual

sudo apt install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common

# add docker's gpg key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

# for x86_64 / amd
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

sudo apt update -y
sudo apt install -y docker-ce

# docker compose
sudo curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# or install docker compose by pip
sudo pip3 install docker-compose

alias dc=docker-compose

# add user to docker groupe
set USER=ubuntu
sudo usermod -aG docker $USER
sudo service docker restart
newgrp - docker

sudo vi /etc/docker/daemon.json

"""
{
  "registry-mirrors": [
    "https://hub-mirror.c.163.com",
    "https://mirror.baidubce.com"
  ]
}
"""
