<?php

require 'config.php';
require 'attack.php';
require 'ban.php';
require 'logger.php';

ban_req_by_ua();
ban_req_by_ip();
log();