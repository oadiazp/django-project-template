FROM ubuntu:18.04

MAINTAINER Omar Antonio Diaz <zcool2005@gmail.com>

ENV DJANGO_SETTINGS_MODULE {{ cookiecutter.project_name }}.settings.live

RUN apt-get update && apt-get upgrade -y

# Set the locale
RUN apt install -y locales
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN apt-get install -y python-virtualenv \
    python3-dev \
    build-essential \
    apt-utils \
    python3-dev \
    gcc \
    libpq-dev \
    libffi-dev \
    zlib1g-dev \ 
    libssl-dev \
    libpcre3-dev \
    sudo \
    nginx

RUN mkdir -p /home/docker/src
RUN virtualenv -p python3 /home/docker/venv

WORKDIR /home/docker/src
RUN rm /etc/nginx/nginx.conf
RUN rm /etc/nginx/sites-enabled/default
COPY conf/uwsgi.ini /home/docker/src
COPY conf/uwsgi_params /home/docker/src
COPY conf/nginx.conf /etc/nginx
COPY conf/nginx-app.conf /etc/nginx/sites-enabled
ADD . .

RUN . /home/docker/venv/bin/activate; \
      pip install -r /home/docker/src/requirements/live/requirements.txt; \
      /home/docker/venv/bin/python /home/docker/src/manage.py collectstatic --clear --traceback --noinput;

RUN chown www-data:www-data -R /home/docker

CMD DJANGO_SETTINGS_MODULE={{ cookiecutter.project_name }}.settings.live /home/docker/venv/bin/python /home/docker/src/manage.py createcachetable & \
    DJANGO_SETTINGS_MODULE={{ cookiecutter.project_name }}.settings.live /home/docker/venv/bin/python /home/docker/src/manage.py migrate & \
    sudo -u www-data /home/docker/venv/bin/uwsgi --ini /home/docker/src/uwsgi.ini & \
    sudo nginx
