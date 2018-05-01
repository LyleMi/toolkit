#!/bin/sh

rsync -avz --progress dbbackup:~/backup /home/dbbackup/backup
