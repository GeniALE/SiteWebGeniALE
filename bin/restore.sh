#!/usr/bin/env bash

output_path="$1"

prefix="docker-compose"

if [ "$output_path" == "prod" ]
then
  prefix="docker-compose -f docker-compose.yml -f docker-compose.prod.yml"
  shift
  output_path="$1"
fi

DOCKER_DB_NAME="$(docker-compose ps -q db)"
DB_HOSTNAME=postgres
DB_USER=postgres

${prefix} up -d db
cat ${output_path} | docker exec -i "${DOCKER_DB_NAME}" psql -U${DB_USER} -d ${DB_HOSTNAME}
${prefix} stop db
