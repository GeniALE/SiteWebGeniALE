#!/usr/bin/env bash
set -e

action="$1"

prefix="docker-compose"

if [ $action == "prod" ]
then
  prefix="docker-compose -f docker-compose.prod.yml"
  shift
  action="$1"
fi

if [ $action == "shell" ]
then
    command="exec web sh"
elif [ $action == "bash" ]
then
    command="exec web bash"
elif [ $action == "exec" ]
then
    command="exec web ${*:2}"
else
    command=" ${*:1}"
fi

eval $prefix $command