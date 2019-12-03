FROM nginx
#对外暴露端口
EXPOSE 80 8080 
#RUN rm /etc/nginx/conf.d/default.conf
RUN mkdir -p /usr/share/nginx/html/static && rm /etc/nginx/conf.d/default.conf
ADD nginx.conf  /etc/nginx/conf.d/
