FROM python:3.10.8-slim-bullseye

WORKDIR /app
COPY . .

RUN apt update && apt upgrade -y && apt install -y gcc
RUN pip install -r requirements.txt

RUN groupadd -g 1000 group && useradd -M -u 1000 user -g 1000
RUN chown -R 1000:1000 /app

USER 1000:1000

CMD uwsgi --ini uwsgi.ini
