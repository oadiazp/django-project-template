from django.apps import AppConfig


class {{ cookiecutter.app_name | capitalize }}Config(AppConfig):
    name = 'apps.{{ cookiecutter.app_name }}'
