# start from base

FROM ubuntu:latest

RUN apt-get update -y && \
    apt-get install -y python3-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "python3", "./config.py" ]
