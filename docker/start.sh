#!/bin/bash

python manage.py migrate
python manage.py collectstatic --no-input --clear
gunicorn --config gunicorn.conf website.wsgi:application --bind 0.0.0.0:8080
