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

sudo apt-get install apache2-utils
sudo htpasswd -c /etc/nginx/.htpasswd user

sudo nginx -t && sudo service nginx restart
