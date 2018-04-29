# install some tool for new machine

sudo apt update && sudo apt upgrade

# make tools
sudo apt install cmake clang

# zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

# peda
sudo apt install gdb
git clone https://github.com/longld/peda.git ~/peda
echo "source ~/peda/peda.py" >> ~/.gdbinit

# pwntools
sudo apt install python-pip python-dev git libssl-dev libffi-dev build-essential
sudo pip install --upgrade pip
sudo pip install --upgrade pwntools

# math
sudo pip install --upgrade opencv-python
sudo pip install --upgrade numpy
sudo pip install --upgrade matplotlib
sudo pip install --upgrade tensorflow
