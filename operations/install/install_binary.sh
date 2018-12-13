#!/bin/sh

# peda
sudo apt install gdb
git clone https://github.com/longld/peda.git ~/peda
echo "source ~/peda/peda.py" >> ~/.gdbinit

git clone git://github.com/Mipu94/peda-heap.git ~/peda-heap
echo "source ~/peda-heap/peda.py" >> ~/.gdbinit

# radare2
git clone https://github.com/radare/radare2.git
./radare2/sys/install.sh
sduo pip install r2pipe

# capstone
sudo pip install capstone

# pwntools
# https://github.com/Gallopsled/pwntools
sudo pip install --upgrade pwntools
# sudo pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -U pwntools
mkdir ~/.pwntools-cache
echo never > ~/.pwntools-cache/update

# ropgadget
sudo pip install --upgrade ropgadget

# pwndbg
git clone https://github.com/pwndbg/pwndbg
cd pwndbg
./setup.sh
