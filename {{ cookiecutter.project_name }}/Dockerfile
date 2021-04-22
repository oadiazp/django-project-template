FROM python:3.9-alpine

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev build-base linux-headers pcre-dev nginx

ENV DJANGO_SETTINGS_MODULE {{ cookiecutter.project_name }}.settings.live

RUN mkdir /app
WORKDIR /app
COPY conf/uwsgi.ini /app
COPY conf/uwsgi_params /app
RUN rm -Rf /etc/nginx/conf.d/default.conf
COPY conf/nginx.conf /etc/nginx
COPY conf/nginx-app.conf /etc/nginx/sites-enabled/app.conf

ADD . .
RUN pip install -r /app/requirements/live/requirements.txt
RUN python manage.py collectstatic --clear --traceback --noinput;

CMD DJANGO_SETTINGS_MODULE={{ cookiecutter.project_name }}.settings.live python /app/manage.py createcachetable & \
    DJANGO_SETTINGS_MODULE={{ cookiecutter.project_name }}.settings.live python /app/manage.py migrate & \
    uwsgi --ini /app/uwsgi.ini & \
    nginx
