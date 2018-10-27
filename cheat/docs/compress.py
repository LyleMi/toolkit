#!/usr/bin/env python
# -*- coding: utf-8 -*-

compressDoc = '''
[tar]

tar xvf fileName.tar
tar cvf fileName.tar dirname

[gz]

gzip -d fileName.gz / gunzip fileName.gz
gzip fileName

[tar.gz / tgz]

tar zxvf fileName.tar.gz
tar zcvf fileName.tar.gz dirName

[bz2]

bzip2 -d fileName.bz2 / bunzip2 fileName.bz2
bzip2 -z fileName

[tar.bz2]

tar jxvf fileName.tar.bz2
tar jcvf fileName.tar.bz2 dirName

[bz] 
bzip2 -d fileName.bz / bunzip2 fileName.bz

[tar.bz]
tar jxvf fileName.tar.bz

[Z]
uncompress fileName.Z
compress fileName

[tar.Z]
tar Zxvf fileName.tar.Z
tar Zcvf fileName.tar.Z dirName

[zip]

unzip fileName.zip
zip fileName.zip dirName

[rar]

rar x fileName.rar
rar a fileName.rar dirName

[lha]

lha -e fileName.lha
lha -a fileName.lha fileName

[rpm]

rpm2cpio fileName.rpm | cpio -div

[deb]

ar p fileName.deb data.tar.gz | tar zxf -

[xz]

xz fileName
xz -d fileName

[tpzx]

pixz fileName
pixz -d fileName
'''


