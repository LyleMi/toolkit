#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docs.base import Base


class Docker(Base):

    _doc = {
        "basic": """
docker build -t name .
docker image ls
docker container ls
docker exec -it bash

docker pull registry.docker-cn.com/library/ubuntu:16.04""",
        "rm": """# rm hang docker
docker container rm $(docker ps -a -q)

# rm untagged/dangling image
docker rmi $(docker images -q -f dangling=true)

# rm all
docker rmi $(docker images -q)""",
        "kill": """docker container kill `docker container ls | awk 'NR==2 {print $1}'`
docker kill $(docker ps -q)""",
        "exec bash": "docker exec -it `docker container ls | awk 'NR==2 {print $1}'` /bin/bash",
        "set iptables for docker": "iptables -I DOCKER-USER -i ext_if ! -s 127.0.0.1 -j DROP",
    }
