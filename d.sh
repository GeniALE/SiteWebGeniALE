#!/usr/bin/env bash
set -e

action="$1"

cmds="shell, exec"
help="You must use one of the follow action: $cmds"
command="echo $help"
prefix="docker-compose"

if [ $action == "prod" ]
then
  prefix="docker-compose -f docker-compose.prod.yml "
  shift
  action="$1"
fi

if [ $action == "shell" ]
then
    command="exec web sh"
elif [ $action == "exec" ]
then
    command="exec web ${*:2}"
elif [ $action == "up ${*:2}" ]
then
    command="up"
elif [ $action == "down ${*:2}" ]
then
    command="down"
elif [ $action == "build" ]
then
    command="build ${*:2}"
fi

eval $prefix $command