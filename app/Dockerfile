FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine

RUN apk --update add bash nano

WORKDIR /app

COPY ./requirements.txt /var/www/requirements.txt
COPY . .

RUN apk add gcc musl-dev python3-dev libffi-dev openssl-dev
RUN pip install -r /var/www/requirements.txt


