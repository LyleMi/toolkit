sudo apt-get install -y golang-go && go version


go env -w GO111MODULE=on
go env -w GOPROXY=https://goproxy.cn,direct
