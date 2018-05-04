#!/bin/sh

# update source if needed
sudo vi /etc/apt/sources.list

# install some tool for new machine
sudo apt update && sudo apt upgrade

# make tools
sudo apt install cmake clang

# python
sudo apt install python-pip python-dev git libssl-dev libffi-dev build-essential

# if apt fail, use easy_install
sudo easy_install pip
sudo pip install --upgrade pip

# zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

# tmux
sudo apt install tmux
git clone https://github.com/gpakosz/.tmux.git
ln -s -f .tmux/.tmux.conf
cp .tmux/.tmux.conf.local .

# peda
sudo apt install gdb
git clone https://github.com/longld/peda.git ~/peda
echo "source ~/peda/peda.py" >> ~/.gdbinit

# pwntools
sudo pip install --upgrade pwntools

# ropgadget
sudo pip install --upgrade ropgadget

# math
sudo pip install --upgrade opencv-python
sudo pip install --upgrade numpy
sudo pip install --upgrade matplotlib
sudo pip install --upgrade tensorflow

# postgresql
sudo apt install postgresql postgresql-contrib
