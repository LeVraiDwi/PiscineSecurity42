FROM ubuntu:latest

WORKDIR /app

RUN apt update
RUN apt upgrade -y
RUN apt install -y curl tor openssh-server
RUN mkdir /var/run/sshd
RUN echo 'root:root123' | chpasswd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -i 's/#Port 22/Port 42/' /etc/ssh/sshd_config

EXPOSE 42

COPY torrc /var/lib/tor/

ENTRYPOINT service ssh start && tor -f /var/lib/tor/torrc