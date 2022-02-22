FROM nginx

RUN mkdir /app

WORKDIR /app

COPY ./pages/app1/* ./app1/
COPY ./pages/app2/* ./app2/
COPY ./pages/app3/* ./app3/

COPY ./configs/* /etc/nginx/conf.d/

