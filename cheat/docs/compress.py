#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .base import BaseDoc


class CompressDoc(BaseDoc):

    _doc = {
        "tar": "tar xvf fileName.tar\ntar cvf fileName.tar dirname",
        "gz": "gzip -d fileName.gz / gunzip fileName.gz\ngzip fileName",
        "tar.gz / tgz": "tar zxvf fileName.tar.gz\ntar zcvf fileName.tar.gz dirName",
        "bz2": "bzip2 -d fileName.bz2 / bunzip2 fileName.bz2\nbzip2 -z fileName",
        "tar.bz2": "tar jxvf fileName.tar.bz2\ntar jcvf fileName.tar.bz2 dirName",
        "bz": "bzip2 -d fileName.bz / bunzip2 fileName.bz",
        "tar.bz": "tar jxvf fileName.tar.bz",
        "Z": "uncompress fileName.Z\ncompress fileName",
        "tar.Z": "tar Zxvf fileName.tar.Z\ntar Zcvf fileName.tar.Z dirName",
        "zip": "unzip fileName.zip\nzip fileName.zip dirName",
        "rar": "rar x fileName.rar\nrar a fileName.rar dirName",
        "lha": "lha -e fileName.lha\nlha -a fileName.lha fileName",
        "rpm": "rpm2cpio fileName.rpm | cpio -div",
        "deb": "ar p fileName.deb data.tar.gz | tar zxf -",
        "xz": "xz fileName\nxz -d fileName",
        "tpzx": "pixz fileName\npixz -d fileName",
        "war": "jar -cvfM0 fileName.war dirName\njar -xvf fileName.war"
    }

if __name__ == '__main__':
    CompressDoc.show()
