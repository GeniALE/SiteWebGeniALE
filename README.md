# SiteWebGeniALE

__Production:__ [![Build Status](https://travis-ci.org/GeniALE/SiteWebGeniALE.svg?branch=master)](https://travis-ci.org/GeniALE/SiteWebGeniALE)

__Development:__ [![Build Status](https://travis-ci.org/GeniALE/SiteWebGeniALE.svg?branch=develop)](https://travis-ci.org/GeniALE/SiteWebGeniALE)

The new website of GeniALE. :beers:
This repository is comprised with two parts, the Content Management System (CMS) and the front-end library for its components. We use *some alien code* and [emojicode](http://www.emojicode.org/).

## Getting Started

Clone this repository

```
git clone git@github.com:GeniALE/SiteWebGeniALE.git
```

### Prerequisites

A [RocketChat](https://rocket.chat/) account to join our chat platform.
Be in the [Trello Website Board](https://trello.com/b/t7NT6LjO/page-web-g%C3%A9niale), where we have all the tasks there.

What things you need to install?
  - Python3 and virtualenv

### Installing

1. Clone the repo `git clone https://github.com/GeniALE/SiteWebGeniALE.git`
2. Go into the directory `cd SiteWebGeniALE`
3. Create your virtual environment: `virtualenv env` 

   **Note**: You must specify python3 if you have multiple Python versions on your system.
4. Activate the env:

    -  `source env/bin/activate` (OSX|POSIX)
    -  `env\Scripts\activate` (Windows).
5. Install dependencies: `pip install -r requirements.txt`
6. Start your **PostgreSQL** database.

    **Note:** If you're using docker, you can run:
     
     - `python cmd.py dockerup` to start the database and 
     - `python cmd.py dockerdown` to stop it.
    
    Local database can be configured with:
     
    - DATABASE_URL
   
   **OR**  
   
    - POSTGRES_USER
    - POSTGRES_DB
    - POSTGRES_PASSWORD
    
6. Run migrations: `python manage.py migrate`
7. Start the website: `python manage.py runserver`

You can use the following credentials by default:

- Username: admin
- Password: admin

If it doesn't work, you can always create a super user like this:

`python manage.py createsuperuser`

## Deployment

To be announced

## Built With

* [NodeJS](https://nodejs.org) - The web framework used

## Contributing

Contact the project leader.

## Versioning

To be seen

## Authors

* **Mathieu Chan Yee Choy** - *Front-line commandant of the semi-colon squad* - [Bazooo](https://github.com/Bazooo)
* **Alexis Côté** - *Do* - [popojargo](https://github.com/popojargo)
* **Cena John** - *you* -
* **Gabriel Bergeron** - *believe* - [gabrielbergeron](https://github.com/gabrielbergeron)
* **Hugo Parent-Leduc** - *in* -
* **Kristian Agbogba** - *Magic?* - [kpucc](https://github.com/kpucc)

See also the list of [contributors](https://github.com/GeniALE/SiteWebGeniALE/contributors) who participated in this project.

## Acknowledgments

* [Club Cedille](https://github.com/clubcedille)
* Inspiration
* etc
