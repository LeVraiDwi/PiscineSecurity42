FROM ubuntu:latest

WORKDIR /app

RUN apt update
RUN apt upgrade -y
RUN apt install -y curl nginx tor

COPY index.html /var/www/html/

EXPOSE 80

CMD [ "nginx", "-c", "/etc/nginx/nginx.conf", "-g", "daemon off;"]