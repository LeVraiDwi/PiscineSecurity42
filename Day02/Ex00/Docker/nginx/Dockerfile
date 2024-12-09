FROM ubuntu:latest

WORKDIR /app

RUN apt update
RUN apt upgrade -y
RUN apt install -y curl nginx tor

RUN rm -rf /etc/nginx/nginx.conf

COPY nginx.conf /etc/nginx/

EXPOSE 80

COPY index.html /www/data/
COPY nginx.conf /app/

CMD [ "nginx", "-c", "/app", "-g", "daemon off;"]
