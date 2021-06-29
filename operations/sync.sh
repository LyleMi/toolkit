#!/bin/bash

# 需要同步的远程服务器
host="remotehost"
# 需要同步远程目录
dest="/root"
git=".git"

inotifywait -mrq --format '%w%f' -e create,modify ./ | while read line
do
    # 考虑到同步目录可能会涉及大量文件，默认不同步目录
    if [ -d $line ]; then
        continue
    fi
    # 包含git的部分不同步
    if [[ $line =~ $git ]]
    then
        continue
    fi
    echo "scp $line $host:$dest/$line"
    scp -rp $line $host:$dest/$line
done
