"""
settings for production mode
"""
from os import environ

import dj_database_url
from django.conf.global_settings import DATABASES
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS  # noqa

from settings.common import *  # noqa

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ROOT_URLCONF = 'urls.project.prod'


# Make this unique, and don't share it with anybody, set it via environment settings.
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# TODO(hoatle): do error warning on prod environment if SECRET_KEY is not provided.

SECRET_KEY = environ.get('SECRET_KEY', SECRET_KEY)

#heroku
# Parse database configuration from $DATABASE_URL
if 'DATABASE_URL' in os.environ:
    DATABASES['default'] = dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']
