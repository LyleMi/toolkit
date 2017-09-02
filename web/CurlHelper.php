<?php

class CurlHelper
{
    public $debug = true;

    public $cookie_jar;

    public function __construct()
    {
        $this->cookie_jar = dirname(__FILE__).'\pic.cookie';
    }

    public function curl_helper($method, $url, $info='', $data=NULL)
    {
        echo $this->colorize($info);

        if($this->debug) {
            echo "data: ";
            var_dump($data);
            echo "url: ";
            var_dump($url);
            echo "method: ";
            var_dump($method);
        } 

        switch ($method) {
            case 'GET':
                $this->rGET($url);
                break;
            case 'POST':
                $this->rPOST($url, $data);
                break;
            case 'PUT':
                $this->rPUT($url, $data);
                break;
            case 'DEL':
                $this->rDELETE($url);
                break; 
            default:
                echo 'Wrong method!';
                break;
        }
    }

    public function colorize($text) {  
        //$text = chr(27) . "[96m" . "$text" . chr(27) . "[0m"; 
        return "\n\n=======================".$text."=======================\n\n";
    }  

    public function rGet($url)
    {       
        $ch = curl_init ();
        curl_setopt ( $ch, CURLOPT_URL, $url );
        curl_setopt ( $ch, CURLOPT_HEADER, 0 );

        //fake ip setting
        curl_setopt($ch, CURLOPT_HTTPHEADER, 
            array(
                'X-FORWARDED-FOR:8.8.8.8', 
                'CLIENT-IP:8.8.8.8'
            ));
        curl_setopt($ch, CURLOPT_REFERER, "http://8.8.8.8");  

        curl_setopt ( $ch, CURLOPT_RETURNTRANSFER, 0 );
        curl_setopt($ch, CURLOPT_COOKIEJAR, $this->cookie_jar);
        curl_setopt($ch, CURLOPT_COOKIEFILE, $this->cookie_jar);
        $ret = curl_exec ( $ch );
        curl_close ( $ch );
        return $ret;
    }

    public function rPOST($url, $data)
    {
        $ch = curl_init ();
        curl_setopt ( $ch, CURLOPT_URL, $url );
        curl_setopt ( $ch, CURLOPT_POST, 1 );
        curl_setopt ( $ch, CURLOPT_HEADER, 0 );
        curl_setopt ( $ch, CURLOPT_RETURNTRANSFER, 0 );
        curl_setopt ( $ch, CURLOPT_POSTFIELDS, http_build_query($data) );
        curl_setopt ( $ch, CURLOPT_COOKIEJAR, $this->cookie_jar);
        curl_setopt ( $ch, CURLOPT_COOKIEFILE, $this->cookie_jar);

        //fake ip setting
        curl_setopt($ch, CURLOPT_HTTPHEADER, 
            array(
                'X-FORWARDED-FOR:8.8.8.8', 
                'CLIENT-IP:8.8.8.8'
            ));
        curl_setopt($ch, CURLOPT_REFERER, "http://8.8.8.8"); 

        $ret = curl_exec ( $ch );
        curl_close ( $ch );
        return $ret;
    }

    public function rPUT($url, $data)
    {   
        $ch = curl_init ();
        
        curl_setopt ( $ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'PUT'); 
        //curl_setopt($ch,CURLOPT_HTTPHEADER,array("X-HTTP-Method-Override: PUT"));
        curl_setopt ( $ch, CURLOPT_HEADER, 0 );
        curl_setopt ( $ch, CURLOPT_RETURNTRANSFER, 0 );
        curl_setopt ( $ch, CURLOPT_POSTFIELDS, http_build_query($data) );
        curl_setopt($ch, CURLOPT_COOKIEFILE, $this->cookie_jar);
        $ret = curl_exec ( $ch );
        curl_close ( $ch );
        return $ret;
    }

    public function rDELETE($url)
    {
        $ch = curl_init ();
        curl_setopt ( $ch, CURLOPT_URL, $url);

        curl_setopt ( $ch, CURLOPT_HEADER, 0 );
        curl_setopt ( $ch, CURLOPT_RETURNTRANSFER, 0 );
        // curl_setopt ( $ch, CURLOPT_TIMEOUT, 5184000 );
        // curl_setopt ( $ch, CURLOPT_CONNECTTIMEOUT, 120 );
        // curl_setopt ( $ch, CURLOPT_NOSIGNAL, true );
        curl_setopt ( $ch, CURLOPT_CUSTOMREQUEST, 'DELETE' );
        curl_setopt($ch, CURLOPT_COOKIEFILE, $this->cookie_jar);
        $ret = curl_exec ( $ch );
        curl_close ( $ch );
        return $ret;
    }

    public function saveCookie()
    {
        //$url = "http://localhost/test.php";
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_HEADER, 0);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 0);
        // curl_setopt ( $ch, CURLOPT_POST, 1 );
        // curl_setopt ( $ch, CURLOPT_POSTFIELDS, http_build_query([1,2]) );
        curl_setopt($ch, CURLOPT_COOKIEJAR, $this->cookie_jar);
        $content = curl_exec($ch);
        curl_close($ch);
        return $content;
    }

    public function checkCookie()
    {
        //$url = "http://localhost/test.php";
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_HEADER, 0);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 0);
        curl_setopt($ch, CURLOPT_COOKIEFILE, $this->cookie_jar);
        $content = curl_exec($ch);
        curl_close($ch);
        return $content;
    } 
}


$curlHelper = new CurlHelper();
$curlHelper->curl_helper(
    'POST',
    'http://question9.erangelab.com/xnucactfwebadmin/logincheck.php',
    '',
    array(
        'username'=>'d0llars',
        'password'=>'username')
    );