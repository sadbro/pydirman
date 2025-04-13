FROM ubuntu:20.04
LABEL authors="Prabaha Das"

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install --no-install-recommends -y python3.9 python3.9-dev python3.9-venv python3-pip python3-wheel build-essential && \
   apt-get clean && rm -rf /var/lib/apt/lists/*
COPY . .

RUN --mount=type=cache,mode=0755,target=/root/.cache pip install -r requirements.txt
RUN cp -n main/pydirman /bin/
RUN cp -n main/reader.out /bin/
RUN cp -n main/pydirman.py /etc/
RUN cp -n main/.pydirman.commands /etc/
RUN chmod 777 /bin/pydirman
RUN chmod 777 /etc/pydirman.py
RUN chmod 777 /bin/reader.out
