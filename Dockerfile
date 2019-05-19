# Dockerization configuration taken from https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/#project-setup
FROM geniale/django-cms-base:latest

# Copy project files. Since our app is not in a subfolder, we need to copy everything manually...
COPY beer_carousel /usr/src/app/beer_carousel
COPY bin /usr/src/app/bin
COPY entrypoint.sh /usr/src/app/
COPY sponsorsModule /usr/src/app/sponsorsModule
COPY static /usr/src/app/static
COPY teamModule /usr/src/app/teamModule
COPY website /usr/src/app/website
COPY manage.py /usr/src/app/

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
