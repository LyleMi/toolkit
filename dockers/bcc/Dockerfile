FROM ubuntu:20.04

RUN rm /etc/apt/sources.list && \
    echo "deb http://mirrors.tencent.com/ubuntu/ focal main restricted universe multiverse" > /etc/apt/sources.list && \
    echo "deb http://mirrors.tencent.com/ubuntu/ focal-security main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb http://mirrors.tencent.com/ubuntu/ focal-updates main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "#deb http://mirrors.tencent.com/ubuntu/ focal-proposed main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "#deb http://mirrors.tencent.com/ubuntu/ focal-backports main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb-src http://mirrors.tencent.com/ubuntu/ focal main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb-src http://mirrors.tencent.com/ubuntu/ focal-security main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb-src http://mirrors.tencent.com/ubuntu/ focal-updates main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "#deb-src http://mirrors.tencent.com/ubuntu/ focal-proposed main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "#deb-src http://mirrors.tencent.com/ubuntu/ focal-backports main restricted universe multiverse" >> /etc/apt/sources.list

RUN apt-get update && \
  DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get install -y bison build-essential cmake flex git libedit-dev \
  libllvm7 llvm-7-dev libclang-7-dev python zlib1g-dev libelf-dev libfl-dev python3-distutils \
  kmod

RUN git clone --depth=1 https://github.com/iovisor/bcc.git

RUN mkdir bcc/build; cd bcc/build && \
  cmake ..  && \
  make -j `nproc` && \
  make install && \
  cmake -DPYTHON_CMD=python3 .. # build python3 binding && \
  pushd src/python/ && \
  make && \
  make install && \
  popd

# apt-get install linux-headers-$(uname -r)
