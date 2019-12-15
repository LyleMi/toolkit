apt install zlib1g-dev libpcre3 libpcre3-dev libbz2-dev libssl-dev libini-config-dev
./auto/configure --prefix=/path/to/nginx --with-select_module
make
./objs/nginx
