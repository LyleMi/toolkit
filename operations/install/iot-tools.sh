#!/bin/sh

# https://github.com/ReFirmLabs/binwalk
# NOTICE: binwalk do not support install via pip
sudo apt-get install python-lzma python3-crypto
sudo pip install nose coverage
git clone --depth=1 https://github.com/ReFirmLabs/binwalk.git

# https://github.com/rampageX/firmware-mod-kit
git clone https://github.com/rampageX/firmware-mod-kit

# https://github.com/firmadyne/firmadyne
