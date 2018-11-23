#!/bin/sh

# http://moloch.3ilson.com/
sudo add-apt-repository ppa:webupd8team/java
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
echo "deb https://artifacts.elastic.co/packages/5.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-5.x.list
sudo apt-get update -y && sudo apt-get upgrade -y && sudo apt-get dist-upgrade -y 

sudo swapoff -a
sudo nano /etc/fstab

echo debconf shared/accepted-oracle-license-v1-1 select true | sudo debconf-set-selections
echo debconf shared/accepted-oracle-license-v1-1 seen true | sudo debconf-set-selections
sudo apt-get install oracle-java8-installer -y
sudo apt-get install elasticsearch -y

wget https://files.molo.ch/builds/ubuntu-16.04/moloch_0.18.2-1_amd64.deb
sudo apt install libwww-perl libjson-perl
sudo dpkg -i moloch_0.18.2-1_amd64.deb

sudo service elasticsearch start
sudo service elasticsearch status

sudo /data/moloch/bin/Configure
sudo /data/moloch/db/db.pl http://localhost:9200 init
sudo /data/moloch/bin/moloch_add_user.sh admin admin PASSWORDGOESHERE --admin
sudo systemctl start molochcapture.service
sudo systemctl start molochviewer.service
