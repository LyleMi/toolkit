#!/bin/sh

sudo apt install -y nodejs npm

npm config set registry https://registry.npm.taobao.org
npm config set registry http://mirrors.cloud.tencent.com/npm/

sudo npm install n -g

# use taobao registry if needed
sudo npm install n -g --registry=https://registry.npm.taobao.org

# change version
sudo n 0.12.2
sudo n stable
sudo n latest

# if npm error, exit shell and retry
# https://stackoverflow.com/questions/33870520/npm-install-cannot-find-module-semver
