git clone https://github.com/GregorR/musl-cross.git
# set TRIPLE in config.sh
# for e.g.
# TRIPLE=mipsel-linux-musl
chmod +x defs.sh
./defs.sh
./clean.sh

sudo apt install -y libmpc-dev
./build.sh
