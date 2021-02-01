# FROM alpine:3.10

# RUN apk add --no-cache python3-dev \
#     && pip3 install --upgrade pip

# WORKDIR /app

# COPY . /app

# RUN pip3 --no-cache-dir install -r requirements.txt
# RUN python -m spacy download es_core_news_sm


# CMD ["python3", "app.py"]

# Docker file for a slim Ubuntu-based Python3 image

FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -y python3-pip python3-dev \
    && cd /usr/local/bin \
    && ln -s /usr/bin/python3 python \
    && pip3 --no-cache-dir install --upgrade pip \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt
RUN python -m spacy download es_core_news_sm


ENTRYPOINT FLASK_APP=/app/app.py flask run --host=0.0.0.0


# ENTRYPOINT ["python3"]