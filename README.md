# SiteWebGeniALE

The new website of GeniALE. :beers:
This repository  contains the CMS and the additionnal modules.

# Table of content
- [SiteWebGeniALE](#sitewebgeniale)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installing](#installing)
  - [Branching model](#branching-model)
- [Deployment](#deployment)
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

A [RocketChat](https://rocket.chat/) account to join our chat platform.
Be in the [Trello Website Board](https://trello.com/b/t7NT6LjO/page-web-g%C3%A9niale), where we have all the tasks there.

What things you need to install?
  - Python3 and virtualenv

## Installing

1. Clone the repo `git clone https://github.com/GeniALE/SiteWebGeniALE.git`
2. Go into the directory `cd SiteWebGeniALE`
3. Create your virtual environment: `virtualenv env` 

   **Note**: You must specify python3 if you have multiple Python versions on your system.
4. Activate the env:

    -  `source env/bin/activate` (OSX|POSIX)
    -  `env\Scripts\activate` (Windows).
5. Install dependencies: `pip install -r requirements.txt`
6. Run migrations: `python manage.py migrate`
7. Start the website: `python manage.py runserver`

You can use the following credentials by default:

- Username: admin
- Password: admin

If it doesn't work, you can always create a super user like this:

`python manage.py createsuperuser`

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

To be announced


# Contributing

Contact the project leader.

# Versioning

To be seen

# Authors

* **Mathieu Chan Yee Choy** - *Front-line commandant of the semi-colon squad* - [Bazooo](https://github.com/Bazooo)
* **Alexis Côté** - *Do* - [popojargo](https://github.com/popojargo)
* **Cena John** - *you* -
* **Gabriel Bergeron** - *believe* - [gabrielbergeron](https://github.com/gabrielbergeron)
* **Hugo Parent-Leduc** - *in* -
* **Kristian Agbogba** - *Magic?* - [kpucc](https://github.com/kpucc)

See also the list of [contributors](https://github.com/GeniALE/SiteWebGeniALE/contributors) who participated in this project.

# Acknowledgments

* Cedille
* Inspiration
* etc
