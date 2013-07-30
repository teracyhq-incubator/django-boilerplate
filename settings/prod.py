"""
settings for production mode
"""
from django.conf.global_settings import DATABASES
from common import *

ROOT_URLCONF = 'urls.project.prod'

# Make this unique, and don't share it with anybody.
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Generate random value from here and get value pasted here: http://www.miniwebtool.com/django-secret-key-generator/
# Changed in Django 1.5: Django will now refuse to start if SECRET_KEY is not set.
SECRET_KEY = ''

#heroku
# Parse database configuration from $DATABASE_URL
if 'DATABASE_URL' in os.environ:
    import dj_database_url
    DATABASES['default'] = dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')