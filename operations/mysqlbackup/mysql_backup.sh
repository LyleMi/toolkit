#!/bin/sh

now="$(date +'%d_%m_%Y_%H_%M_%S')"
filename="db_backup_$now".gz
backupfolder="/home/dbbackup/backup"
fullpath="$backupfolder/$filename"

DB_USER="backup"
DB_PASS="db_pass"
DB_NAME="db_name"

mysqldump -u $DB_USER -p$DB_PASS --single-transaction $DB_NAME | gzip > "$fullpath"
