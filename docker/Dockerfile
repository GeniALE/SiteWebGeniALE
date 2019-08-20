# Dockerization configuration taken from https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/#project-setup
FROM geniale/django-cms-base:latest

# Install NGINX and other dependencies
RUN apk update
RUN apk add bash \
	nginx \
	supervisor

# Copy project files. Since our app is not in a subfolder, we need to copy everything manually...
COPY docker/gunicorn.conf \
   manage.py \
   docker/start.sh \
   docker/entrypoint.sh \
   /usr/src/app/

# Copy folders
COPY bin /usr/src/app/bin
COPY beer_carousel /usr/src/app/beer_carousel
COPY sponsorsModule /usr/src/app/sponsorsModule
COPY teamModule /usr/src/app/teamModule
COPY website /usr/src/app/website

# Copy other configuration files for Nginx...
COPY docker/supervisor-app.conf /etc/supervisor/conf.d/
COPY docker/nginx.conf /etc/nginx/nginx.conf
COPY docker/nginx-app.conf /etc/nginx/sites-available/default

# Create folder for static files collected
RUN mkdir -p /usr/src/app/static
RUN rm /etc/nginx/conf.d/default.conf

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

CMD ["supervisord", "-n", "-c", "/etc/supervisor/conf.d/supervisor-app.conf"]
