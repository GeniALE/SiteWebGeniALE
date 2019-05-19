# django-cms-base

![Docker automated](https://img.shields.io/docker/cloud/automated/geniale/django-cms-base.svg)![Docker automated build status](https://img.shields.io/docker/cloud/build/geniale/django-cms-base.svg)![Docker image size](https://img.shields.io/microbadger/image-size/geniale/django-cms-base/latest.svg)


This is the base image for our web container.

It extends a `python:3.5-alpine` and install all the latest requirements for our website.


## Install

You can install the image using:

```bash
docker pull geniale/django-cms-base:latest
```

---

## Internal

When you change the requirements of the website, you will need to update them in the
docker base image. To do so, you must first login:

```bash
docker login
```

### Build

```bash
docker build -f docker/base/Dockerfile -t geniale/django-cms-base:latest .
```

### Push

```bash
docker push -t geniale/django-cms-base:latest
```