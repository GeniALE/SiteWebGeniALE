# SiteWebGeniALE

**Production:** [![Build Status](https://travis-ci.org/GeniALE/SiteWebGeniALE.svg?branch=master)](https://travis-ci.org/GeniALE/SiteWebGeniALE)

**Development:** [![Build Status](https://travis-ci.org/GeniALE/SiteWebGeniALE.svg?branch=develop)](https://travis-ci.org/GeniALE/SiteWebGeniALE)

The new website of GeniALE. :beers:
This repository  contains the CMS and the additional modules.

# Table of content
- [SiteWebGeniALE](#sitewebgeniale)
- [Table of content](#table-of-content)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installing](#installing)
  - [Branching model](#branching-model)
    - [Feature workflow](#feature-workflow)
    - [Fix workflow](#fix-workflow)
- [Deployment](#deployment)
  - [Production deployment](#production-deployment)
- [Plugins](#plugins)
- [Documentation](#documentation)
- [Authors](#authors)
- [Acknowledgments](#acknowledgments)
- [Licenses](#licenses)
  - [Owl carousel](#owl-carousel)

# Getting Started

Clone this repository

```
git clone git@github.com:GeniALE/SiteWebGeniALE.git
```

## Prerequisites

A [Slack](https://slack.com/) account to join our chat platform.
Be in the [Trello Website Board](https://trello.com/b/t7NT6LjO/page-web-g%C3%A9niale), where we have all the tasks there.

Otherwise, here are the prerequisites:

- [Python 3.5](https://www.python.org/downloads/release/python-350/)
- [PostgreSQL 10 and later](https://www.postgresql.org/) 

## Installing

If you wish to use docker,  see the [Docker documentation](docs/DOCKER.md).

If you wish to use Pycharm, see the [Pycharm documentation](docs/PYCHARM.md).

Otherwise, here's the classic configuration with a terminal:

1. Create the database in PostgreSQL: (eg: `geniale_website`)
2. Clone the repo `git clone https://github.com/GeniALE/SiteWebGeniALE.git`
3. Go into the directory `cd SiteWebGeniALE`
4. You need to create a `.env` file to store your environment variables.
    
    You can also copy `.env.example` to `.env`.
    
    It contains some of the default env variables. Then, modify the values to fit your database configuration.
    
    > *Note: As this file is mandatory, you don't have to put variables in it. As long as it exists, it's fine.*
5. Create your virtualenv: `virtualenv -p python3 venv`
6. Activate your virtual env:
    
    - **Windows**: `env\Scripts\activate`
    - **POSIX**: `source env/bin/activate`
    
7. Install the dependencies: `pip3 install -r requirements.txt`
8. Run the migrations `python3 manage.py migrate`
9. Create a superuser: `python3 manage.py createsuperuser`
10. Run the server: `python3 manage.py runserver 0.0.0.0` 
7. The DjangoCMS should be running at [http://localhost:8000](localhost:8000)

## Branching model

For this project, we are using a branching model that focus on continuous delivery.

Basically, you have those type of branches :

- **master** : Trunk or latest branch
- **feature** : New feature development based on **master**
- **fix** : A fix for something in master. 

### Feature workflow

- Create your feature branch from the master with a `feature/` prefix.
- Do your work
- Rebase master into your branch
- Review and test 
- Create pull request
- Set the reviewers for your pull request (you must have at least **ONE** approval to merge)
- Assign the pull request to the person in charge of merging (*it can be yourself*)
- Assign your Trello card to the same person you assigned the PR
- Merge the branch when you have your approvals

### Fix workflow

When we find a flaw, we have to respond quickly to fix that bug.

The workflow is pretty much the same.
 
The only difference is the branch prefix: `fix/`.

# Deployment

At the moment, the website is deployed at: http://geniale-cms.herokuapp.com/

## Production deployment

1. Pull the repository
2. Install the dependencies: 
    
    ```shell
    pip install -r requirements.txt```
3. Create the environment configuration: `cp .env.example .env`
4. Modify the environment configuration and set the database credentials.
5. Start the server

    ```shell
    python manage.py migrate && python manage.py runserver 0.0.0.0:80
    ```

# Plugins

- [Team module](teamModule/README.md)
- [Beer carousel](beer_carousel/README.md)
- [Sponsors Module](sponsorsModule/README.md)

# Documentation

- [**Backups**](docs/BACKUPS.md)
- [**Docker**](docs/DOCKER.md)
- [**Pycharm**](docs/PYCHARM.md)
- [**Translations**](docs/TRANSLATIONS.md)

# Authors

- **William Cantin** [:octocat:](https://github.com/wilomgfx)
- **Mathieu Chan Yee Choy** [:octocat:](https://github.com/Bazooo)
- **Alexis Côté** [:octocat:](https://github.com/popojargo)
- **Gabriel Bergeron** [:octocat:](https://github.com/gabrielbergeron)
- **Alexandre Desgagné** [:octocat:](https://github.com/alexemdesgagne)
- **Hugo Parent-Leduc** [:octocat:](https://github.com/hugoparent)
- **Kristian Agbogba** [:octocat:](https://github.com/kpucc)

See also the list of [contributors](https://github.com/GeniALE/SiteWebGeniALE/contributors) who participated in this project.

# Acknowledgments

* [Club Cedille](https://github.com/clubcedille)

# Licenses

## Owl carousel

The code and the documentation are released under the [MIT License](static/lib/owlcarousel/LICENSE).
