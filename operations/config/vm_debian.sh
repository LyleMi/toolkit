# disable daily apt update
systemctl mask apt-daily.service apt-daily-upgrade.service
systemctl disable apt-daily.service apt-daily-upgrade.service
systemctl disable apt-daily.timer apt-daily-upgrade.timer
