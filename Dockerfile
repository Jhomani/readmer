# RUN AS
#
# docker build -t readmer .
# docker run -ti -v $(pwd):/home/admin/readmer readmer bash
# grouID  < `$ id -g` userID  < `$ id -u`

FROM alpine:3.15

ENV GID 1001
ENV UID 1000

RUN apk add --no-cache bash python3 py3-pip

RUN addgroup -S swali -g $GID && \
    adduser -S admin -u $UID -G swali -s /bin/bash

WORKDIR /home/admin/readmer

COPY requirements.txt . 

RUN pip install -r requirements.txt 

USER admin
