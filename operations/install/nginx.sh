apt install zlib1g-dev libpcre3 libpcre3-dev libbz2-dev libssl-dev libini-config-dev
./auto/configure --prefix=/path/to/nginx --with-select_module
make
./objs/nginx

# cert
openssl genrsa -out ca-key.pem 4096
openssl req -new -key ca-key.pem -out ca-req.csr -subj "/C=CN/ST=BJ/L=BJ/O=fish/OU=fish/CN=CA"
openssl x509 -req -in ca-req.csr -out ca-cert.pem -signkey ca-key.pem -days 3650
openssl genrsa -out server-key.pem 4096
openssl req -new -out server-req.csr -key server-key.pem -subj "/C=CN/ST=BJ/L=BJ/O=fish/OU=fish/CN=*.example.com"
openssl x509 -req -in server-req.csr -out server-cert.pem -signkey server-key.pem -CA ca-cert.pem -CAkey ca-key.pem -CAcreateserial -days 3650

# one line
mkdir -p /etc/ssl/private/
sudo openssl req -x509 -nodes -days 3650 -newkey rsa:4096 -keyout ./certs/nginx-selfsigned.key -out ./certs/nginx-selfsigned.crt

<< _EOF_
# nginx ssl setting
ssl_protocols TLSv1 TLSv1.1 TLSv1.2 TLSv1.3; # Dropping SSLv3, ref: POODLE
ssl_prefer_server_ciphers on;
ssl_certificate /etc/ssl/certs/nginx-selfsigned.crt;
ssl_certificate_key /etc/ssl/private/nginx-selfsigned.key;
_EOF_

sudo apt-get install -y apache2-utils
# or
sudo yum install -y httpd-tools
sudo htpasswd -c /etc/nginx/.htpasswd user

<< _EOF_
auth_basic "auth";
auth_basic_user_file /etc/nginx/.htpasswd;
_EOF_

sudo nginx -t && sudo service nginx restart
