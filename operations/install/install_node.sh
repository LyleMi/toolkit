#!/bin/sh

sudo apt install -y nodejs

sudo npm install n -g

# use taobao registry if needed
sudo npm install n -g --registry=https://registry.npm.taobao.org

# change version
sudo n 0.12.2
sudo n stable
sudo n latest
