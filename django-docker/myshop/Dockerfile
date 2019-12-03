FROM python:3.6
RUN mkdir -p /app/myshop
WORKDIR /app/myshop 
COPY pip.conf /root/.pip/pip.conf
ADD . /app/myshop
RUN pip3 install -r requirements.txt 
EXPOSE 80 8080 
ENV SPIDER=/app/myshop
