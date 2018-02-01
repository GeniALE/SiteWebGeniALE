#!/usr/bin/env bash
# wait-for-postgres.sh
# Taken from: https://docs.docker.com/compose/startup-order/
set -e

host="$1"
shift
cmd="$@"

export PGPASSWORD=geniale
until psql -h "$host" -U "postgres" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up"