# Dockerization configuration taken from https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/#project-setup
FROM geniale/django-cms-base:latest

# Copy project files. Since our app is not in a subfolder, we need to copy everything manually...
COPY beer_carousel /usr/src/app/beer_carousel
COPY docker/gunicorn.conf /usr/src/app
COPY bin /usr/src/app/bin
COPY docker/entrypoint.sh /usr/src/app/
COPY sponsorsModule /usr/src/app/sponsorsModule
COPY teamModule /usr/src/app/teamModule
COPY website /usr/src/app/website
COPY manage.py /usr/src/app/

# Create folder for static files collected
RUN mkdir -p /usr/src/app/static

# run entrypoint.prod.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
