#!/bin/sh

# peda
sudo apt install -y gdb
git clone --depth=1 https://github.com/longld/peda.git ~/peda
echo "source ~/peda/peda.py" >> ~/.gdbinit

# peda-heap
git clone --depth=1 https://github.com/Mipu94/peda-heap.git ~/peda-heap
echo "source ~/peda-heap/peda.py" >> ~/.gdbinit

# radare2
git clone --depth=1 https://github.com/radare/radare2.git
./radare2/sys/install.sh
sduo pip install r2pipe

# unicron
git clone --depth=1 https://github.com/unicorn-engine/unicorn
UNICORN_ARCHS="arm aarch64 x86 mips" ./make.sh
sudo ./make.sh install
sudo ./make.sh uninstall

# capstone
sudo pip install capstone

# pwntools/
# https://github.com/Gallopsled/pwntools
# sudo pip install --upgrade pwntools
sudo apt-get install -y python3 python3-pip python3-dev git libssl-dev libffi-dev build-essential
python3 -m pip install pwntools
# sudo python3 -m pip install --upgrade git+https://github.com/Gallopsled/pwntools.git@dev
# sudo pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -U pwntools
mkdir ~/.pwntools-cache
echo never > ~/.pwntools-cache/update

# ropgadget
sudo pip install --upgrade ropgadget

# pwndbg
git clone --depth=1 https://github.com/pwndbg/pwndbg
cd pwndbg
./setup.sh

# exploitable
git clone --depth=1 https://github.com/jfoote/exploitable
source ~/exploitable/exploitable/exploitable.py
exploitable

# angr
sudo pip install angr
