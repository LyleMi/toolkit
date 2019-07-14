#!/bin/sh

git clone http://git.php.net/repository/php-src.git
cd php-src
./buildconf
./configure --disable-all --enable-debug --prefix=$HOME/php-debug
make -j4
make install
