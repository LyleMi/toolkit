<?php

require_once "/tmp/logger.php"

define("LONE_LINE", '\n'.str_repeat('=', 21).'\n');

$ip = $_SERVER["REMOTE_ADDR"];
$method = $_SERVER['REQUEST_METHOD'];
$uri = $_SERVER['REQUEST_URI'];
$headers = getallheaders();

@$request = print_r($_REQUEST, true);
@$cookie = print_r($_COOKIE, true);
@$file = print_r($_FILE, true);
@$post = file_get_contents('php://input');

$data = date('Y-m-d H:i:s:u') . '\n';
$data .= "$method $uri\n";
$data .= "headers\n";

foreach ($headers as $name => $value) {
    $data .= "$name : $value \n";
}

if(strlen($post)) $data .= "post data\n$post\n";
if(strlen($request)) $data .= "request\n$request\n";
if(strlen($cookie)) $data .= "cookie\n$cookie\n";
if(strlen($file)) $data .= "file\n$file";

file_put_contents(__dir__ . '/log', 
    $data . LONE_LINE, FILE_APPEND);
