#!/bin/sh

rpm -Uvh http://mirror.webtatic.com/yum/el5/latest.rpm #CentOs 5.x
rpm -Uvh http://mirror.webtatic.com/yum/el6/latest.rpm #CentOs 6.x
rpm -Uvh https://mirror.webtatic.com/yum/el7/epel-release.rpm #CentOs 7.X
rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm

yum install php70w
