#!/bin/sh

sudo adduser dbbackup
su dbbackup
crontab -e
# /bin/bash /home/dbbackup/mysql_backup.sh
