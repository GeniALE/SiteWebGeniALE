# Assumes the database container is named 'db'

DOCKER_DB_NAME="$(docker-compose ps -q db)"
DB_HOSTNAME=postgres
DB_USER=postgres
LOCAL_DUMP_PATH="website-2018-07-15.sql"

docker-compose up -d db
docker exec -i "${DOCKER_DB_NAME}" pg_restore -C --clean --no-acl --no-owner -U "${DB_USER}" -d "${DB_HOSTNAME}" < "${LOCAL_DUMP_PATH}"
docker-compose stop db
