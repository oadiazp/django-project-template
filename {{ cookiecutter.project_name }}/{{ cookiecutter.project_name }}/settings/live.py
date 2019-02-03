from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'pgsql',
        'USER': 'postgres',
        'PASSWORD': 's7RXvwMyR9WfQmx88evkhUk85',
        'NAME': '{{ cookiecutter.project_name }}',
        'ATOMIC_REQUESTS': True,
    }
}

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
