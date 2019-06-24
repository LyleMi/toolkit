FROM ubuntu:last

ENV AFL_INSTALL http://lcamtuf.coredump.cx/afl/releases/afl-latest.tgz

# afl:
#   build-essential, wget

RUN apt-get update --quiet && apt-get install --yes \
        --no-install-recommends \
        --no-install-suggests \
    autoconf \
    automake \
    gcc \
    libtool \
    make \
    nasm \
    subversion \
    wget \
# Clean up packages.
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Get ready to build.
WORKDIR /tmp

# Get and build AFL.
RUN \
    wget \
    $AFL_INSTALL \
        --no-verbose \
    && mkdir afl-src \
    && tar -xzf afl-latest.tgz \
        -C \
        afl-src \
        --strip-components=1 \
    && cd afl-src \
    && sed -i 's/^\/\/ #define USE_64BIT/#define USE_64BIT/gI' config.h \
    && make \
    && make install \
    && rm -rf \
        /tmp/afl-latest.tgz \
        /tmp/afl-src
