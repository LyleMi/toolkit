<?php

require_once "/tmp/php-waf.php"

define("LONE_LINE", str_repeat('=', 21));

assert_options(ASSERT_ACTIVE, false);

$ip = $_SERVER["REMOTE_ADDR"];
$method = $_SERVER['REQUEST_METHOD'];
$uri = $_SERVER['REQUEST_URI'];
$headers = getallheaders();
@$request = print_r($_REQUEST, true);
@$cookie = print_r($_COOKIE, true);
@$file = print_r($_FILE, true);
@$post = file_get_contents('php://input');

$data = "$method $uri\n";

foreach ($headers as $name => $value) {
    $data .= "$name : $value \n";
}

if(strlen($post)) $data .= "php input\n$post\n";
if(strlen($request)) $data .= "request\n$request\n";
if(strlen($cookie)) $data .= "cookie\n$cookie\n";
if(strlen($file)) $data .= "file\n$file";
$data = date('Y-m-d H:i:s:u') . '\n' . $data;


file_put_contents(__dir__ . '/log', "$requests\n\n$response\n" . LONE_LINE . "\n", FILE_APPEND);
