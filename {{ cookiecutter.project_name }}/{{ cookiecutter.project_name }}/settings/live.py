from .base import * # noqa
from apps.utils import get_secret
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration


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

sentry_sdk.init(
    dsn="{{ cookiecutter.sentry_url }}",
    integrations=[DjangoIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production,
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True,

    # By default the SDK will try to use the SENTRY_RELEASE
    # environment variable, or infer a git commit
    # SHA as release, however you may want to set
    # something more human-readable.
    # release="myapp@1.0.0",
)

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
