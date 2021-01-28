#!/bin/bash
docker pull mysql:5.7 
docker pull redis
docker pull python:3.7
docker-compose build
docker-compose up -d
exit
#docker-compose exec storage bash
#查看集群状态
#fdfs_monitor /etc/fdfs/storage.conf
#重启tracker的nginx
#/usr/bin/nginx -s reload
