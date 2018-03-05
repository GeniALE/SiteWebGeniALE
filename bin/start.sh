#!/usr/bin/env bash

if [ -z ${PORT+x} ]
then
  PORT=8000
fi

python manage.py migrate && python manage.py runserver 0.0.0.0:$PORT