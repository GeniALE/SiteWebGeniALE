# Set the base image for the docker to python v3.6
FROM python:3.6

# Force stdin, stdout and stderr to be totally unbuffered
ENV PYTHONUNBUFFERED 1

# Install psql for scripts
RUN apt-get update && apt-get install postgresql-client-9.4 -y

# Create directory code in the docker
RUN mkdir /code

# Cd into code to work into
WORKDIR /code

# Copy the requirements.txt from the repo to the code directory
ADD requirements.txt /code/

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the repo files into the WORKDIR
ADD website /code/website
ADD manage.py /code/
ADD bin /code/bin
