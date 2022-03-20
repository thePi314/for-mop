FROM python:3.9-buster

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN apt-get update -y && apt-get install build-essential python-dev -y
RUN pip install -r requirements.txt

COPY ./compose/staging/entrypoint /entrypoint
RUN chmod +x /entrypoint

ADD . /code/

WORKDIR /code

ENTRYPOINT ["/entrypoint"]