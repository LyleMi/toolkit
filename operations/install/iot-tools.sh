#!/bin/sh

# https://github.com/ReFirmLabs/binwalk
# NOTICE: binwalk do not support install via pip
sudo apt-get install python-lzma python3-crypto
sudo pip install nose coverage
git clone --depth=1 https://github.com/ReFirmLabs/binwalk.git

# https://github.com/rampageX/firmware-mod-kit
sudo apt-get install -y git build-essential zlib1g-dev liblzma-dev python-magic
git clone https://github.com/rampageX/firmware-mod-kit

# https://github.com/firmadyne/firmadyne

git clone https://github.com/craigz28/firmwalker

# cross compile

git clone https://github.com/GregorR/musl-cross.git

# Modify or set the following variables in config.sh
CFLAGS="-fPIC"

# For little-endian MIPS, perform the following:
'''
set TRIPLE=mipsel in config.sh
run ./clean.sh to clean out any previous builds
run ./build.sh to build and install the toolchain into /opt/cross
'''

# For big-endian MIPS, perform the following:
'''
set TRIPLE=mipseb in config.sh
set LINUX_HEADERS_URL=https://kernel.org/pub/linux/kernel/v2.6/longterm/v2.6.32/linux-2.6.32.70.tar.xz in defs.sh
run ./clean.sh to clean out any previous builds
run ./build.sh to build and install the toolchain into /opt/cross
'''

# For little-endian ARM, perform the following:
'''
set TRIPLE=armeabi, GCC_BOOTSTRAP_CONFFLAGS="--with-arch=armv6 --with-float=softfp", and GCC_CONFFLAGS="--with-arch=armv6 --with-float=softfp" in config.sh
set LINUX_HEADERS_URL=https://kernel.org/pub/linux/kernel/v4.x/linux-4.1.17.tar.xz in defs.sh
run ./clean.sh to clean out any previous builds
run ./build.sh to build and install the toolchain into /opt/cross
'''

# You should have the following directories, or wherever you installed the toolchains:
'''
/opt/cross/arm-linux-musleabi
/opt/cross/mipseb-linux-musl
/opt/cross/mipsel-linux-musl
'''
