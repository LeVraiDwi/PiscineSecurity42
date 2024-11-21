FROM ubuntu:latest

WORKDIR /app

RUN apt update
RUN apt upgrade -y
RUN apt install -y curl nginx tor

EXPOSE 80

COPY index.html /usr/share/nginx/html/

CMD [ "nginx", "-g", "daemon off;"]