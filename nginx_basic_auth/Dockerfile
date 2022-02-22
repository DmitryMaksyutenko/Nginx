FROM nginx:latest

WORKDIR /app

COPY . .
COPY ./default.conf /etc/nginx/conf.d/
COPY ./.htpassw /etc/nginx/
