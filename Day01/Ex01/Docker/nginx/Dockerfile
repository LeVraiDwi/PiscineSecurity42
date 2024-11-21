FROM ubuntu:latest

WORKDIR /app

RUN apt update
RUN apt upgrade -y
RUN apt install -y curl nginx tor

COPY torrc /var/lib/tor/
COPY index.html /usr/share/nginx/html/

RUN nginx -s start &

CMD [ "tor", "-f", "/var/lib/tor/torrc"]