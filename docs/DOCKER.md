# Docker setup

You can setup your project to use docker.

- [Docker setup](#docker-setup)
- [Prerequisites](#prerequisites)
- [Getting started](#getting-started)
- [Base image](#base-image)
- [Developer setup](#developer-setup)
  - [Docker files](#docker-files)
- [Production deployment](#production-deployment)
  - [Docker files](#docker-files-1)
- [Docker tools](#docker-tools)


# Prerequisites

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

# Getting started

1. You need to create a `.env` file to store your docker environment.
    
    You can also copy `.env.docker-example` to `.env`. It contains some of the default env variables.
    
    *Note: As this file is mandatory, you don't have to put variables in it. As long as it exists, it's fine.*
2. Build the docker containers `docker-compose build`
3. Run the docker services `docker-compose up`
4. The DjangoCMS should be running at [http://localhost:8000](localhost:8000)
5. You need to create your super user with:

    `docker-compose run web python manage.py createsuperuser`
   
# Base image

The base image of our web container is located in [docker/base](docker/base).
Its a prebuild Python 3.5-alpine image with libsass dependencies.

Its used to speedup the usage of docker.
 
# Developer setup

The developer setup consists of a `docker-compose` configuration that combines:

- A PostgreSQL database (**db**) mounted on `pgdata_dev`
- A web container for DjangoCMS (**web**) mount on `.`

You can run the setup with: `docker-compose up` or `./d.sh up`

The developer setup serve the static/media files via Python. It also mount the 
local directory directly in the container. So every local changes will be reflected in the container.

## Docker files

- `Dockerfile`: The Dockerfile for the web container.
- `docker-compose.yml`: The base configuration for all docker-compose setups.
- `docker-compose.override.yml`: The developer setup override configuration file.


# Production deployment

The production setup consists of a `docker-compose` configuration that combines:

- A PostgreSQL database (**db**) mounted on `pgdata`
- A web container for DjangoCMS (**web**) running Gunicorn.
- A Nginx server to serve static files


1. Pull the repository
2. Build docker compose 
    
    `docker-compose -f docker-compose.yml -f docker-compose.prod.yml build` or `./d.sh prod build`
3. Start docker compose 

    `docker-compose -f docker-compose.yml -f docker-compose.prod.yml up` or `./d.sh prod up`

## Docker files

- `docker/Dockerfile`: The Dockerfile for the production web container.
- `docker/nginx`: A directory containing Nginx Dockerfile and configuration files.
- `docker/gunicorn.conf`: A Gunicorn configuration file to allow setting config 
via environment variable prefixed by `GUNICORN_`.
- `docker-compose.yml`: The base configuration for all docker-compose setups.
- `docker-compose.prod.yml`: The production configuration for docker-compose

    
# Docker tools

At the root of the repository, you can find a script called `d` 

This script is a shortcut for some of the docker commands.

You can always run any command on your docker-compose with: `d <command>`

To run command on production, you need to run: `d prod <command>`

| Command | Description                         | POSIX              | WIN              |
|---------|-------------------------------------|--------------------|------------------|
| shell   | Open a shell into the web container | ./d.sh shell          | d shell          |
| exec    | Execute something in the container  | ./d.sh exec python -V | d exec python -V |
| bash    | Execute a bash terminal in the container | ./d.sh bash | d bash | 
Eventually, more commands will be added to automate some tasks.
    