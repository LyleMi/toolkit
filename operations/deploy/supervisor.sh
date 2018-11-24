#!/bin/sh

pip install -U supervisor

mkdir -p /etc/supervisor/conf.d
mkdir -p /var/log/supervisord/

echo_supervisord_conf > /etc/supervisor/supervisord.conf

sed -i "s/;\[include\]/[include]\nfiles = conf.d\/*.conf/g" /etc/supervisor/supervisord.conf

projectName="projectName"
# command to be executed
command="ls"
# directory to execute command
commandDir="/tmp/ls"

cd /etc/supervisor/conf.d/

echo "[program: $projectName]" >> $projectName.conf
echo "command=$command" >> $projectName.conf
echo "directory=$commandDir" >> $projectName.conf
# will auto restart
echo "autorestart=true" >> $projectName.conf
# will auto start
echo "autostart=true" >> $projectName.conf
# error log
echo "stderr_logfile=/var/log/supervisord/$projectName.err.log" >> $projectName.conf
# output log
echo "stdout_logfile=/var/log/supervisord/$projectName.out.log" >> $projectName.conf
# environment
echo "environment=ENVIRONMENT=Production" >> $projectName.conf
# execute user
echo "user=root" >> $projectName.conf
echo "stopsignal=INT" >> $projectName.conf
echo "startsecs=1" >> $projectName.conf

# start program
supervisord -c /etc/supervisor/supervisord.conf
supervisorctl start $projectName
ps -ef | grep $projectName

# stop all
supervisorctl shutdown

# stop program
supervisorctl stop $projectName

# check status
supervisorctl status
