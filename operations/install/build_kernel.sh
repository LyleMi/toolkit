#!/bin/sh

# debian
sudo apt-get install libncurses5-dev libncursesw5-dev

# centos
sudo yum install -y ncurses-devel ncurses elfutils-libelf-devel openssl-devel bc

# https://www.kernel.org/
VERSION=4.9.145
wget https://cdn.kernel.org/pub/linux/kernel/v4.x/linux-$VERSION.tar.xz
tar xvJf linux-$VERSION.tar.xz

# choice one
# text based config
make config
# text menu based config
make menuconfig
make xconfig
make oldconfig
