FROM ubuntu:16.04

MAINTAINER {{ cookiecutter.author }} <{{ cookiecutter.email }}>

ENV DJANGO_SETTINGS_MODULE {{ cookiecutter.project_name }}.settings.{{ env }}

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
    python3.5-dev \
    gettext \
    gcc \
    libpq-dev \
    libffi-dev \ 
    npm \ 
    ruby-full \
    zlib1g-dev \ 
    libssl-dev \
    libpcre3-dev \
    git \
    sudo

RUN mkdir /home/docker
RUN virtualenv -p python3 /home/docker/venv

RUN mkdir /root/.ssh
RUN mkdir /home/docker/src

COPY conf/uwsgi.ini /home/docker/src
COPY conf/uwsgi_params /home/docker/src

WORKDIR /home/docker/src

ADD . .

RUN . /home/docker/venv/bin/activate; \
      pip install -r /home/docker/src/requirements/{{ env }}.txt;

#RUN ln -s /usr/bin/nodejs /usr/bin/node
#RUN ln -s /node_modules/coffee-script/bin/coffee /usr/bin/coffee
#
#RUN apt-get install -y yui-compressor
#RUN gem install sass
#
#RUN coffee -c .
#RUN sass --update apps/core/static/sass:apps/core/static/sass

RUN . /home/docker/venv/bin/activate; \
#    python /home/docker/src/manage.py compilemessages; \
    python /home/docker/src/manage.py collectstatic --clear --traceback --noinput;

RUN chown www-data:www-data -R /home/docker

CMD DJANGO_SETTINGS_MODULE={{ cookiecutter.project_name }}.settings.{{ env }} /home/docker/venv/bin/python /home/docker/src/manage.py createcachetable & \
    sudo -u www-data /home/docker/venv/bin/uwsgi --ini /home/docker/src/uwsgi.ini
    
