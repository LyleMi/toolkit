<?php

$banuas = [
    "appscan",
    "sqlmap",
    "nessus",
    "netsparker",
    "webinspect",
    "webreaver",
    "wvs",
];

// $ua = strtolower($_SERVER["HTTP_USER_AGENT"]);
$ua = 'sqlmap';

foreach ($banuas as $banua) {
    if (strpos($ua, $banua) !== false) {
        die("waf");
    }
}

function sendBomb()
{
    // dd if=/dev/zero bs=1M count=1024 | gzip > 1G.gzip
    //prepare the client to recieve GZIP data. This will not be suspicious
    //since most web servers use GZIP by default
    header("Content-Encoding: gzip");
    header("Content-Length: " . filesize('1G.gzip'));
    //Turn off output buffering
    if (ob_get_level()) {
        ob_end_clean();
    }

    //send the gzipped file to the client
    readfile('1G.gzip');
}
