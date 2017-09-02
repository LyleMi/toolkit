<?php

function clean_hash($hash)
{
    return preg_replace("/[^0-9a-f]/", "", $hash);
}

function myhash($str)
{
    return clean_hash(md5(md5($str) . "SALT"));
}

function psgen($i)
{
    $str = '';
    $str .= '0123456789';
    $str .= 'abcdefghijklmnopqrstuvwxyz';
    $str .= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';

    $len = strlen($str);

    $val = '';
    while ($i > 0) {
        $t = $i % $len;
        $i -= $t;
        $i = intval($i / $len);
        $val .= $str[$t];
    }
    return $val;
}

for ($i = 0; $i < 100000000000; $i++) {
    $t = psgen($i);
    $md = myhash($t);
    if (substr($md, 0, 2) == "0e" && ctype_digit(substr($md, 2, 30))) {
        echo $t . '<br />';
        echo $md . '<br />';
        exit();
    }
}
