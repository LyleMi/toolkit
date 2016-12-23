<?php

define("LONE_LINE", str_repeat('=', 21));

$method = $_SERVER['REQUEST_METHOD'];
$uri = $_SERVER['REQUEST_URI'];
$headers = getallheaders();
$request = print_r($_REQUEST, true);
$cookie = print_r($_COOKIE, true);
$file = print_r($_FILE, true);
@$post = file_get_contents('php://input');

$data = "$method $uri\n";

foreach ($headers as $name => $value) {
    $data .= "$name : $value \n";
}

$data .= "\n $post";

file_put_contents(__dir__ . '/log', "$requests\n\n$response\n" . LONE_LINE . "\n", FILE_APPEND);
