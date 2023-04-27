# Dockerfile

# Author       : ledeXb
# Github       : https://github.com/ledeXb
# Messenger    : https://m.me/LedeXb
# Email        : ghbartw@gmail.com
# Date         : 26-04-2023
# Main Language: Python

# Download and import main images

# Operating system
FROM debian:latest
# Main package
FROM python:3

# Author info
LABEL MAINTAINER="https://github.com/ledeXb/Fishing.git"

# Working directory
WORKDIR Fishing/
# Add files 
ADD . /Fishing

# Installing other packages
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install php openssh-client -y
RUN pip3 install -r files/requirements.txt
RUN apt-get clean

# Main command
CMD ["python3", "Fishing.py", "--noupdate"]

## Wanna run it own? Try following commnads:

## "sudo docker build . -t kasroudra/Fishing:latest", "sudo docker run --rm -it kasroudra/Fishing:latest"

## "sudo docker pull kasroudra/Fishing", "sudo docker run --rm -it kasroudra/Fishing"
