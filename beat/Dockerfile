FROM python:3.9
WORKDIR /usr/src/app

#RUN apk add --no-cache --virtual \
#        .build-deps \
#        gcc \
#        g++ \
#        musl-dev \
#        python3-dev
#
#RUN rm  -rf /tmp/* /var/cache/apk/*

COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt

COPY ./app /usr/src/app
