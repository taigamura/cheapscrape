# base image ubuntu 20.04
FROM ubuntu:20.04

WORKDIR /work
COPY . /work

# install dependencies
RUN apt-get update && apt-get install -y \
    software-properties-common

RUN add-apt-repository universe

RUN apt-get update && apt-get install -y \
    apache2 \
    curl \
    git \
    python3.6 \
    python3-pip
    
# pip dependencies
RUN pip3 install \
    beautifulsoup4

# ! Useful CMD:
# * Build: docker build -t env-ubuntu .
# ? Bindmount: docker run -it -v C:/dev/env-ubuntu/dev:/work/dev env-ubuntu
# ? Foreground (Interact with CLI): docker run -it env-ubuntu
# * ctrl + d to exit