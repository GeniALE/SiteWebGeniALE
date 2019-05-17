# Dockerization configuration taken from https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/#project-setup
# Set the base image for the docker to python v3.5
FROM python:3.5-alpine

# set work directory
WORKDIR /usr/src/app

# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && apk add jpeg-dev zlib-dev \
    && pip install psycopg2 \
    && apk del build-deps

# Install dependencies
COPY ./requirements.txt /usr/src/app/requirements.txt

RUN apk add --no-cache --virtual build-deps build-base linux-headers \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

# copy project
COPY . /usr/src/app/

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
