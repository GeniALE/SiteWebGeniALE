# Dockerization configuration taken from https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/#project-setup
FROM geniale/django-cms-base:latest

# Copy project files. Since our app is not in a subfolder, we need to copy everything manually...
COPY entrypoint.sh \
  manage.py \
  /usr/src/app/

# Copy other folders
COPY beer_carousel /usr/src/app/beer_carousel
COPY bin /usr/src/app/bin
COPY sponsorsModule /usr/src/app/sponsorsModule
COPY teamModule /usr/src/app/teamModule
COPY orchester_cms_integration /usr/src/app/orchester_cms_integration
COPY website /usr/src/app/website

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
