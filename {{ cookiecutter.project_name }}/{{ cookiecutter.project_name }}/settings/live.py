from .base import *
from apps.utils import get_secret

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': get_secret('DB_HOST'),
        'USER': get_secret('DB_USER'),
        'PASSWORD': get_secret('{{ cookiecutter.project_name|upper }}_DB_PASSWORD'),
        'NAME': get_secret('DB_NAME'),
        'ATOMIC_REQUESTS': True,
    }
}

SECRET_KEY = get_secret('{{ cookiecutter.project_name|upper }}_SECRET_KEY'),

INSTALLED_APPS += [
    'raven.contrib.django.raven_compat',
]

# import raven
#
# VERSION = '0.1'

# RAVEN_CONFIG = {
#     'dsn': 'https://0110f857397d4e1c8c6473dccb085fed:2769b5d3d1f440eda1eaf4109fa02caa@sentry.io/1197976',
#     # If you are using git, you can also automatically configure the
#     # release based on the git info.
#     'release': VERSION,
# }

DEBUG = False

# EMAIL_HOST = 'smtp.mandrillapp.com'
# EMAIL_HOST_USER = 'CubaTramites'
# EMAIL_HOST_PASSWORD = 'XSlvFyqDdGF749mvbK45tA'
# EMAIL_PORT = '587'
# EMAIL_USE_TLS = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
