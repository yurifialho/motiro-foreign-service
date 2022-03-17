FROM python:3.9

RUN mkdir /init.db
COPY ./docker/init.db/ /init.db/

WORKDIR /usr/src/app
ADD ./requirements.txt /
RUN pip install -r /requirements.txt 
ADD app .

CMD uwsgi --enable-threads --ini uwsgi.ini