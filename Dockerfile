FROM alpine:latest
LABEL MAINTAINER="https://github.com/ledeXb/Fishing.git"
WORKDIR /Fishing/
ADD . /Fishing
RUN apk add --no-cache bash ncurses curl unzip wget php 
CMD "./Fishing.sh"
