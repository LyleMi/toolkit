<?php


function ban_req_by_ua() {

    $ua = strtolower($_SERVER["HTTP_USER_AGENT"]);

    foreach ($banuas as $banua) {
        if (strpos($ua, $banua) !== false) {
            die(sendBomb());
        }
    }
}

function ban_req_by_ip() {

    $ip = $_SERVER["REMOTE_ADDR"];

    foreach ($banips as $banip) {
        if ($banip == $ip) {
            die();
        }
    }

}