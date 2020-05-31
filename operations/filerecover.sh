#!/bin/sh

sudo yum -y install bzip2 e2fsprogs-devel e2fsprogs
sudo apt install -y bzip2 e2fsprogs e2fslibs-dev

git clone https://git.code.sf.net/p/extundelete/code extundelete
cd extundelete

CFLAGS="-static" CXXFLAGS="-static" ./configure
make && make install

./src/extundelete --inode 2 /dev/vdb
