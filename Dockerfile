FROM ubuntu:18.04

WORKDIR /opt
COPY . /opt

USER root
ENV IRODS_USER=anonymous

RUN apt-get update && apt-get install -y \
    apt-transport-https \
    gcc \
    gnupg \
    wget 

RUN wget https://files.renci.org/pub/irods/releases/4.1.10/ubuntu14/irods-icommands-4.1.10-ubuntu14-x86_64.deb \
   && apt-get install -y ./irods-icommands-4.1.10-ubuntu14-x86_64.deb

RUN apt-get update
RUN apt-get install -y python3.6\
                       python3-pip \
                       wget \
                       build-essential \
                       software-properties-common \
                       apt-utils \
                       ffmpeg \
                       libsm6 \
                       libxext6

RUN apt-get update
RUN apt-get install -y libgdal-dev
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN ldconfig
RUN apt-get install -y locales && locale-gen en_US.UTF-8
ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8'

ENTRYPOINT [ "python3.6", "/opt/data_pull.py" ]

