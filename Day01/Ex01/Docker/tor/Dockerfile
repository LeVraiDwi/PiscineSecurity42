FROM ubuntu:latest

WORKDIR /app

RUN apt update
RUN apt upgrade -y
RUN apt install -y curl tor

COPY torrc /var/lib/tor/

CMD [ "tor", "-f", "/var/lib/tor/torrc"]