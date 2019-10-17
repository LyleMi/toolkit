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
