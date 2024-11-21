FROM ubuntu:latest

WORKDIR /app

RUN apt update
RUN apt upgrade -y
RUN apt install -y curl nginx tor

EXPOSE 80

CMD [ "nginx", "-g", "daemon off;"]