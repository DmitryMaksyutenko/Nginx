FROM nginx

RUN rm /etc/nginx/conf.d/default.conf

COPY ./server1/server1.conf /etc/nginx/conf.d/
COPY ./server2/server2.conf /etc/nginx/conf.d/
COPY ./server3/server3.conf /etc/nginx/conf.d/

WORKDIR /apps

COPY . .
