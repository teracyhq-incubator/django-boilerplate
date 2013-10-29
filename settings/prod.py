"""
settings for production mode
"""
from os import environ

import dj_database_url
from django.conf.global_settings import DATABASES

from settings.common import *  # noqa

ROOT_URLCONF = 'urls.project.prod'

# Make this unique, and don't share it with anybody, set it via environment settings.
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key

SECRET_KEY = environ.get('SECRET_KEY', SECRET_KEY)

#heroku
# Parse database configuration from $DATABASE_URL
if 'DATABASE_URL' in os.environ:
    DATABASES['default'] = dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
