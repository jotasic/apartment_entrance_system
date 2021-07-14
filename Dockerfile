FROM python:3.8
WORKDIR  /usr/src/app
COPY . /usr/src/app
RUN apt-get install -y --no-install-recommends \
    default-libmysqlclient-dev
RUN pip install -r requirements.txt