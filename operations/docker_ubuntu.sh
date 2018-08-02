#!/bin/sh

# https://docs.docker.com/install/linux/docker-ce/ubuntu/

sudo apt remove docker docker-engine docker.io

# for ubuntu 14.x
sudo apt install linux-image-extra-$(uname -r) linux-image-extra-virtual

sudo apt install \
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

sudo apt update
sudo apt install docker-ce

# docker compose
sudo curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# or install docker compose by pip
sudo pip install docker-compose
