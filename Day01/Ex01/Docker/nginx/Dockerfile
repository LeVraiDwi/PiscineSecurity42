FROM ubuntu:latest

WORKDIR /app

RUN apt update
RUN apt upgrade -y
RUN apt install -y curl nginx tor

RUN rm -rf /etc/nginx/nginx.conf

COPY nginx.conf /etc/nginx/

EXPOSE 80

CMD [ "nginx", "-g", "daemon off;"]
