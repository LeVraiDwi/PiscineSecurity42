FROM ubuntu:latest

WORKDIR /app

RUN apt update
RUN apt upgrade -y
RUN apt install -y curl nginx tor

COPY index.html /usr/share/nginx/html/

CMD [ "nginx", "-g", "daemon off;"]