FROM python:3.7
RUN mkdir -p /myshop && mkdir -p /root/.pip
WORKDIR /myshop
ADD . /myshop
COPY pip.conf /root/.pip/pip.conf
#COPY /py-packages/django /usr/local/lib/python3.7/site-packages/
#COPY /home/lja/Desktop/proj_1/py-packages/Django-3.0.7.dist-info /usr/local/lib/python3.7/site-packages/
#COPY /home/lja/Desktop/proj_1/py-packages/haystack /usr/local/lib/python3.7/site-packages/
RUN pip install -r requirements.txt 
EXPOSE 8080