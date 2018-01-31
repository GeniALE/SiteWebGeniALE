#!/usr/bin/env bash
set -e

action="$1"

cmds="shell, exec"
help="You must use one of the follow action: $cmds"
command="echo $help"

if [ $action == "shell" ]
then
    command="docker-compose exec web sh"
elif [ $action == "exec" ]
then
    command="docker-compose exec web ${*:2}"
fi

eval $command