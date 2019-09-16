# SiteWebGeniALE

**Production:** [![Build Status](https://travis-ci.org/GeniALE/SiteWebGeniALE.svg?branch=master)](https://travis-ci.org/GeniALE/SiteWebGeniALE)

**Development:** [![Build Status](https://travis-ci.org/GeniALE/SiteWebGeniALE.svg?branch=develop)](https://travis-ci.org/GeniALE/SiteWebGeniALE)

The new website of GeniALE. :beers:
This repository  contains the CMS and the additional modules.

# Table of content
- [SiteWebGeniALE](#SiteWebGeniALE)
- [Table of content](#Table-of-content)
- [Getting Started](#Getting-Started)
  - [Prerequisites](#Prerequisites)
  - [Installing](#Installing)
  - [Branching model](#Branching-model)
- [Deployment](#Deployment)
  - [Production deployment](#Production-deployment)
- [Plugins](#Plugins)
- [Documentation](#Documentation)
- [Authors](#Authors)
- [Acknowledgments](#Acknowledgments)
- [Licenses](#Licenses)
  - [Owl carousel](#Owl-carousel)

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

<details><summary>Basic installation</summary>
<p>

Before starting, you need to create a database for the website. You can either
use the create a database from the [terminal](https://stackoverflow.com/questions/30641512/create-database-from-command-line) or 
with a GUI such as [PGAdmin](https://www.youtube.com/watch?v=h05bcVYcGRU)

Clone the Github repository

```bash
  git clone https://github.com/GeniALE/SiteWebGeniALE.git
```

Create an `.env` file with your configurations

```bash
cd SiteWebGeniALE
cp .env.example .env
```

>**Note**: You might want to change the values according to your environment configurations.

Create your virtualenv

```bash
virtualenv -p python3 venv
```

Each time you want to work on your project, you need to activate your environment:

On Unix like OS:
```bash
source env/bin/activate
```

On Windows: 
```cmd
env\Scripts\activate
```

Install dependencies, migrations and create super user

```bash
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py createsuperuser
```

You can finally start the server with:

```bash
python3 manage.py runserver 0.0.0.0
```

The website should be running at [http://localhost:8080](localhost:8080)
</p>
</details>

## Branching model

For this project, we are using a branching model that focus on continuous delivery.

Basically, you have those type of branches :

- **master** : Trunk or latest branch
- **feature** : New feature development based on **master**
- **fix** : A fix for something in master. 

<details><summary>Feature workflow</summary>
<p>

- Create your feature branch from the master with a `feature/` prefix.
- Do your work
- Rebase master into your branch
- Review and test 
- Create pull request
- Set the reviewers for your pull request (you must have at least **ONE** approval to merge)
- Assign the pull request to the person in charge of merging (*it can be yourself*)
- Assign your Trello card to the same person you assigned the PR
- Merge the branch when you have your approvals

</p>
</details>

<details><summary>Fix workflow</summary>
<p>

When we find a flaw, we have to respond quickly to fix that bug.

The workflow is pretty much the same.
 
The only difference is the branch prefix: `fix/`.

</p>
</details>

# Deployment

At the moment, the website is deployed at: http://geniale-cms.herokuapp.com/

## Production deployment

1. Pull the repository
2. Install the dependencies: 
    
    ```shell
    pip install -r requirements.txt
    ```
3. Create the environment configuration: `cp .env.example .env`
4. Modify the environment configuration and set the database credentials.
5. To use Orchester, you need to create a `.orchester.json` configuration file with the
proper credentials. For more details, refers to that documentation: https://github.com/popojargo/orchester
6. Start the server

    ```shell
    python manage.py migrate && python manage.py runserver 0.0.0.0:80
    ```

# Plugins

- [Team module](teamModule/README.md)
- [Beer carousel](beer_carousel/README.md)
- [Sponsors Module](sponsorsModule/README.md)
- [Orchester integration module](orchester_cms_integration/README.md)

# Documentation

- [**Backups**](docs/BACKUPS.md)
- [**Docker**](docs/DOCKER.md)
- [**Pycharm**](docs/PYCHARM.md)
- [**Translations**](docs/TRANSLATIONS.md)

# Authors

- **Gabriel Bergeron** [:octocat:](https://github.com/gabrielbergeron)
- **William Cantin** [:octocat:](https://github.com/wilomgfx)
- **Mathieu Chan Yee Choy** [:octocat:](https://github.com/Bazooo)
- **Alexis Côté** [:octocat:](https://github.com/popojargo)
- **Alexandre Desgagné** [:octocat:](https://github.com/alexemdesgagne)

See also the list of [contributors](https://github.com/GeniALE/SiteWebGeniALE/contributors) who participated in this project.

# Acknowledgments

* **Club Cedille** [:octocat:](https://github.com/clubcedille)[:globe_with_meridians:](http://cedille.etsmtl.ca/)

# Licenses

## Owl carousel

The code and the documentation are released under the [MIT License](website/static/lib/owlcarousel/LICENSE).
