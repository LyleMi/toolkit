#!/bin/sh

# https://github.com/WhaleShark-Team/cobra

# Mac
brew install grep findutils flex phantomjs

# Ubuntu
apt-get install flex bison phantomjs

# Centos
yum install flex bison phantomjs

git clone https://github.com/WhaleShark-Team/cobra.git && cd cobra
pip install -r requirements.txt
python cobra.py --help
