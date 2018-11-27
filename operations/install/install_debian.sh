#!/bin/sh

# update source if needed
# sudo vi /etc/apt/sources.list

echo '# Tsinghua deb source \n\
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial main restricted universe multiverse  \n\
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-updates main restricted universe multiverse \n\
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse \n\
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-security main restricted universe multiverse'  >> /etc/apt/sources.list

# install some tool for new machine
sudo apt update && sudo apt upgrade -y

# make tools
sudo apt install cmake clang

# python
sudo apt install python-pip python-dev git libssl-dev libffi-dev build-essential

# if apt fail, use easy_install
sudo easy_install pip
sudo pip install --upgrade pip

# zsh
# https://github.com/robbyrussell/oh-my-zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
sed -i 's/ZSH_THEME="robbyrussell"/ZSH_THEME="bira"/' ~/.zshrc
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
git clone https://github.com/zsh-users/zsh-history-substring-search ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-history-substring-search
sed -i 's/^plugins=(/plugins=(\n  zsh-autosuggestions\n  zsh-syntax-highlighting\n  zsh-history-substring-search/' ~/.zshrc
source ~/.zshrc

# vim
curl "https://raw.githubusercontent.com/LyleMi/toolkit/master/operations/config/.vimrc" > ~/.vimrc

# tmux
sudo apt install tmux
git clone https://github.com/gpakosz/.tmux.git
ln -s -f .tmux/.tmux.conf
cp .tmux/.tmux.conf.local .

# postgresql
sudo apt install postgresql postgresql-contrib

# the fuck
# https://github.com/nvbn/thefuck
sudo apt install python3-dev python3-pip
sudo pip3 install thefuck

# https configure
git clone https://github.com/certbot/certbot
cd ./certbot
./certbot-auto

