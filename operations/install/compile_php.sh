#!/bin/sh

VERSION=$(wget -qO- http://php.net/downloads.php | grep -m 1 h3 | cut -d '"' -f 2 | cut -d "v" -f 2)
wget http://am1.php.net/distributions/php-$VERSION.tar.gz
tar xvf php-$VERSION.tar.gz
rm php-$VERSION.tar.gz
cd php-$VERSION
./configure CFLAGS="-g -O0"
make
make test
sudo make install
