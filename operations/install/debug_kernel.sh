#!/bin/sh

# debian
sudo apt-get install libncurses5-dev libncursesw5-dev

# centos
sudo yum install -y ncurses-devel ncurses \
    elfutils-libelf-devel openssl-devel bc qemu seabios \
    glibc-static

# https://www.kernel.org/
VERSION=4.9.145
wget https://cdn.kernel.org/pub/linux/kernel/v4.x/linux-$VERSION.tar.xz
tar xvJf linux-$VERSION.tar.xz

# choice one
# config: text based config
# menuconfig: text menu based config
make config
make menuconfig
make xconfig
make oldconfig

# Kernel hacking 
#   Compile-time
#      [*] Compile the kernel with debug info
#       [*] Compile the kernel with frame pointers
#   [*] KGDB:kernel debugging with remote gdb
#   [ ] Write protect kernel read-only data structures
# Processor type and features
#   Linux guest support
#      [ ] Paravirtualized guest support

make

# busybox
git clone https://github.com/mirror/busybox.git
cd busybox

make menuconfig
# select Busybox Settings -> Build Options -> Build Busybox as a static binary
# exclude Linux System Utilities -> [] Support mounting NFS file system
# exclude Networking Utilities -> [] inetd
make install

cd _install
mkdir proc sys dev etc etc/init.d
echo '#!/bin/sh
mount -t proc none /proc
mount -t sysfs none /sys
/sbin/mdev -s' > etc/init.d/rcS
chmod +x etc/init.d/rcS
find . | cpio -o --format=newc > ../rootfs.img

# busybox end

qemu-system-x86_64 -kernel ./linux-$VERSION/arch/x86_64/boot/bzImage \
    -initrd ./busybox/rootfs.img \
    -append "console=ttyS0 root=/dev/ram rdinit=/sbin/init" \
    -cpu kvm64,+smep,+smap --nographic -gdb tcp::1234
