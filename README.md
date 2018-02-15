# SiteWebGeniALE

__Production:__ [![Build Status](https://travis-ci.org/GeniALE/SiteWebGeniALE.svg?branch=master)](https://travis-ci.org/GeniALE/SiteWebGeniALE)

__Development:__ [![Build Status](https://travis-ci.org/GeniALE/SiteWebGeniALE.svg?branch=develop)](https://travis-ci.org/GeniALE/SiteWebGeniALE)

The new website of GeniALE. :beers:
This repository  contains the CMS and the additionnal modules.

# Table of content
- [SiteWebGeniALE](#sitewebgeniale)
- [Table of content](#table-of-content)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installing](#installing)
  - [Branching model](#branching-model)
- [Deployment](#deployment)
  - [Production deployment](#production-deployment)
  - [Docker tools](#docker-tools)
- [Contributing](#contributing)
- [Versioning](#versioning)
- [Authors](#authors)
- [Acknowledgments](#acknowledgments)

# Getting Started

Clone this repository

```
git clone git@github.com:GeniALE/SiteWebGeniALE.git
```

## Prerequisites

A [Slack](https://slack.com/) account to join our chat platform.
Be in the [Trello Website Board](https://trello.com/b/t7NT6LjO/page-web-g%C3%A9niale), where we have all the tasks there.

What things you need to install?
  - Docker & docker-compose

## Installing

1. Clone the repo `git clone https://github.com/GeniALE/SiteWebGeniALE.git`
2. Go into the directory `cd SiteWebGeniALE`
3. Build the docker containers `docker-compose build`
4. Run the docker services `docker-compose up`
5. The DjangoCMS should be running at [http://localhost:8000](localhost:8000)
6. You need to create your super user with:

    `docker-compose run web python manage.py createsuperuser`

7. If you want, you can create a `.env` file to setup some environment variables.
 
    You can copy the `.env.default` as an example.
## Branching model

For this project, we are using Git Flow.

Basically, you have those type of branches :

- **master** : Production
- **release** : Releases are created from **develop** and merged into **master**.
- **develop** : Features merged but not ready for prod yet.
- **feature** : New feature development based on **develop**
- **hotfix** : A fix for something in production. (Merge back to **develop** and **master**

For more details, look [at this amazing cheatsheet](https://danielkummer.github.io/git-flow-cheatsheet/)

# Deployment

At the moment, the website is deployed at: http://geniale-prod.herokuapp.com/

## Production deployment

1. Pull the repository
2. Build docker compose 
    
    `docker-compose -f docker-compose.prod.yml build` or `./d.sh prod build`
3. Start docker compose 

    `docker-compose -f docker-compose.prod.yml up` or `./d.sh prod up`
    
## Docker tools

At the root of the repostiory, you can find a script called `d` 

This script is a shortcut for some of the docker commands.

You can always run any command on your docker-compose with: `d <command>`

To run command on production, you need to run: `d prod <command>`

| Command | Description                         | POSIX              | WIN              |
|---------|-------------------------------------|--------------------|------------------|
| shell   | Open a shell into the web container | ./d shell          | d shell          |
| exec    | Execute something in the container  | ./d exec python -V | d exec python -V |

Eventually, more commands will be added to automate some tasks.

# Contributing

Contact the project leader.

# Versioning

To be seen

# Authors

* **Mathieu Chan Yee Choy** [Bazooo](https://github.com/Bazooo)
* **Alexis Côté** [popojargo](https://github.com/popojargo)
* **Gabriel Bergeron** [gabrielbergeron](https://github.com/gabrielbergeron)
* **Hugo Parent-Leduc** [hugoparent](https://github.com/hugoparent)
* **Kristian Agbogba** [kpucc](https://github.com/kpucc)

See also the list of [contributors](https://github.com/GeniALE/SiteWebGeniALE/contributors) who participated in this project.

# Acknowledgments

* [Club Cedille](https://github.com/clubcedille)
* Inspiration
* etc
