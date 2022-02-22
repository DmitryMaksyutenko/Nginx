FROM python:3.10

RUN mkdir /app

WORKDIR /app

COPY . .

RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip install gunicorn
