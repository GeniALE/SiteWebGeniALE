#!/usr/bin/env bash
ACTION="$1"

prefix="docker-compose"

if [ "$ACTION" == "prod" ]
then
  prefix="docker-compose -f docker-compose.yml -f docker-compose.prod.yml"
  shift
  ACTION="$1"
fi


NOW=`date +%Y-%m-%d"_"%H_%M_%S`
DOCKER_DB_NAME=$(${prefix} ps -q db)
DB_HOSTNAME=postgres
DB_USER=postgres

if [ -z ${ACTION} ]
then
    ACTION="website-${NOW}.sql"
fi

${prefix} up -d db
docker exec -i "${DOCKER_DB_NAME}" pg_dumpall -c -U "${DB_USER}" > "${ACTION}"
${prefix} stop db
