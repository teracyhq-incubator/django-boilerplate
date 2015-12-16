# -*- coding:utf-8 -*-

# Copyright (c) Teracy, Inc. and individual contributors.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
#     1. Redistributions of source code must retain the above copyright notice,
#        this list of conditions and the following disclaimer.
#
#     2. Redistributions in binary form must reproduce the above copyright
#        notice, this list of conditions and the following disclaimer in the
#        documentation and/or other materials provided with the distribution.
#
#     3. Neither the name of Teracy, Inc. nor the names of its contributors may be used
#        to endorse or promote products derived from this software without
#        specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""
This is a simple library that sets configuration defaults for
Heroku-esque environment variables.

Thanks to https://github.com/kennethreitz/flask-heroku/

Usage
-----

Add the following code snippet on manage.py, wsgi.py for bootstrapping.

```
import heroku_env
heroku_env.set_env()
```

it's recommended to use django-dotenv to load .env variables for development mode.

```
import dotenv
dotenv.read_dotenv()
```

Installation
------------

$ pip install django-heroku-env

"""

from os import environ

try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

from envparse import env
import dj_database_url
from django.conf import settings

from env_vars import env_vars, setting_value, cast_bool, cast_eval


def set_env():
    """Set, Override settings values"""
    env_vars.add(
        # project
        PROJECT_NAME=dict(default='Project'),
        # sites
        SITE_DOMAIN=dict(default=None, ignore_none=True),
        SITE_NAME=dict(default=None, ignore_none=True),
        # emails
        DEFAULT_FROM_EMAIL=dict(default=None, ignore_none=True),
        EMAIL_SUBJECT_PREFIX=dict(default=None, ignore_none=True),
        EMAIL_BACKEND=dict(default=None, ignore_none=True),
        SERVER_EMAIL=dict(default=None, ignore_none=True),
        EMAIL_HOST=dict(default=None, ignore_none=True),
        EMAIL_PORT=dict(default=None, ignore_none=True),
        EMAIL_HOST_USER=dict(default=None, ignore_none=True),
        EMAIL_HOST_PASSWORD=dict(default=None, ignore_none=True),
        EMAIL_USE_TLS=dict(cast=cast_bool, default=None, ignore_none=True),
        EMAIL_USE_SSL=dict(cast=cast_bool, default=None, ignore_none=True),
        EMAIL_SSL_KEYFILE=dict(default=None, ignore_none=True),
        EMAIL_SSL_CERTFILE=dict(default=None, ignore_none=True),
        EMAIL_TIMEOUT=dict(default=None, ignore_none=True),
        # admins, managers
        ADMINS=dict(cast=cast_eval, default=None, ignore_none=True),
        MANAGERS=dict(cast=cast_eval, default=None, ignore_none=True),
        # Sentry
        SENTRY_DSN=dict(default=None),
        # Exceptional
        EXCEPTIONAL_API_KEY=dict(default=None),
        # GoogleFed
        GOOGLE_DOMAIN=dict(default=None),
        # Celery w/ RabbitMQ or Celery w/ RedisCloud
        BROKER_URL=[dict(name='CLOUDAMQP_URL', only_if='CLOUDAMQP_URL'),
                    dict(name='RABBITMQ_URL', only_if='RABBITMQ_URL'),
                    dict(name='REDISCLOUD_URL', only_if='REDISCLOUD_URL')],
        BROKER_TRANSPORT=dict(name='BROKER_TRANSPORT', only_if='BROKER_TRANSPORT')
    )

    # DATABASE_URL
    setting_value('DATABASES', {'default': dj_database_url.config()})

    # Mailgun
    if 'MAILGUN_SMTP_SERVER' in environ:
        setting_value('MAILGUN_API_KEY', env('MAILGUN_API_KEY'))
        setting_value('MAILGUN_DOMAIN', env('MAILGUN_DOMAIN'))
        setting_value('MAILGUN_PUBLIC_KEY', env('MAILGUN_PUBLIC_KEY'))
        setting_value('MAILGUN_SMTP_LOGIN', env('MAILGUN_SMTP_LOGIN'))
        setting_value('MAILGUN_SMTP_PASSWORD', env('MAILGUN_SMTP_PASSWORD'))
        setting_value('MAILGUN_SMTP_PORT', env('MAILGUN_SMTP_PORT', cast=int))
        setting_value('MAILGUN_SMTP_SERVER', env('MAILGUN_SMTP_SERVER'))

        use_mail_gun_api = env('MAILGUN_USE_API', cast=cast_bool, default=True)
        use_mail_gun_smtp = env('MAILGUN_USE_SMTP', cast=cast_bool, default=True)

        # for use api
        if use_mail_gun_api:
            # django-mailgun:
            setting_value('MAILGUN_ACCESS_KEY', settings.MAILGUN_API_KEY)
            setting_value('MAILGUN_SERVER_NAME', settings.MAILGUN_DOMAIN)

        if use_mail_gun_smtp:
            # for django smtp server: use smtp
            setting_value('EMAIL_HOST', settings.MAILGUN_SMTP_SERVER)
            setting_value('EMAIL_PORT', settings.MAILGUN_SMTP_PORT)
            setting_value('EMAIL_HOST_USER', settings.MAILGUN_SMTP_LOGIN)
            setting_value('EMAIL_HOST_PASSWORD', settings.MAILGUN_SMTP_PASSWORD)
            setting_value('MAIL_USE_TLS', env('MAIL_USE_TLS', cast=cast_bool, default=True))

    # SendGrid
    if 'SENDGRID_USERNAME' in environ:
        # this is enough to use https://github.com/elbuo8/sendgrid-django
        # don't forget to set EMAIL_BACKEND
        setting_value('SENDGRID_USERNAME', env('SENDGRID_USERNAME'))
        setting_value('SENDGRID_PASSWORD', env('SENDGRID_PASSWORD'))
        setting_value('SENDGRID_API_KEY', env('SENDGRID_API_KEY', default=None))

        setting_value('SENDGRID_SMTP_LOGIN', env('SENDGRID_SMTP_LOGIN',
                                                 default=settings.SENDGRID_USERNAME))
        setting_value('SENDGRID_SMTP_PASSWORD', env('SENDGRID_SMTP_PASSWORD',
                                                    default=settings.SENDGRID_PASSWORD))
        setting_value('SENDGRID_SMTP_PORT', env('MAILGUN_SMTP_PORT', cast=int,
                                                default=587), )
        setting_value('SENDGRID_SMTP_SERVER', env('SENDGRID_SMTP_SERVER',
                                                  default='smtp.sendgrid.net'))

        send_grid_use_smtp = env('SENDGRID_USE_SMTP', cast=cast_bool, default=True)

        if send_grid_use_smtp:
            setting_value('EMAIL_HOST', settings.SENDGRID_SMTP_SERVER)
            setting_value('EMAIL_PORT', settings.SENDGRID_SMTP_PORT)
            setting_value('EMAIL_HOST_USER', settings.SENDGRID_SMTP_LOGIN)
            setting_value('EMAIL_HOST_PASSWORD', settings.SENDGRID_SMTP_PASSWORD)
            setting_value('MAIL_USE_TLS', env('MAIL_USE_TLS', cast=cast_bool, default=True))

    # Postmark
    # if 'POSTMARK_SMTP_SERVER' in environ:
    #     setting_value('SMTP_SERVER', 'POSTMARK_SMTP_SERVER')
    #     setting_value('SMTP_LOGIN', environ.get('POSTMARK_API_KEY'))
    #     setting_value('SMTP_PASSWORD', environ.get('POSTMARK_API_KEY'))
    #     setting_value('MAIL_SERVER', 'POSTMARK_SMTP_SERVER')
    #     setting_value('MAIL_USERNAME', environ.get('POSTMARK_API_KEY'))
    #     setting_value('MAIL_PASSWORD', environ.get('POSTMARK_API_KEY'))
    #     setting_value('MAIL_USE_TLS', True)

    # Redis To Go
    redis_url = environ.get('REDISTOGO_URL')
    if redis_url:
        url = urlparse(redis_url)
        setting_value('REDIS_HOST', url.hostname)
        setting_value('REDIS_PORT', url.port)
        setting_value('REDIS_PASSWORD', url.password)

    # Mongolab
    mongolab_uri = environ.get('MONGOLAB_URI')
    if mongolab_uri:
        url = urlparse(mongolab_uri)
        setting_value('MONGO_URI', mongolab_uri)
        setting_value('MONGODB_USER', url.username)
        setting_value('MONGODB_USERNAME', url.username)
        setting_value('MONGODB_PASSWORD', url.password)
        setting_value('MONGODB_HOST', url.hostname)
        setting_value('MONGODB_PORT', url.port)
        setting_value('MONGODB_DB', url.path[1:])

    # MongoHQ
    mongohq_uri = environ.get('MONGOHQ_URL')
    if mongohq_uri:
        url = urlparse(mongohq_uri)
        setting_value('MONGO_URI', mongohq_uri)
        setting_value('MONGODB_USER', url.username)
        setting_value('MONGODB_PASSWORD', url.password)
        setting_value('MONGODB_HOST', url.hostname)
        setting_value('MONGODB_PORT', url.port)
        setting_value('MONGODB_DB', url.path[1:])

    # Cloudant
    cloudant_uri = environ.get('CLOUDANT_URL')
    if cloudant_uri:
        setting_value('COUCHDB_SERVER', cloudant_uri)

    # Memcachier
    setting_value('CACHE_MEMCACHED_SERVERS', env('MEMCACHIER_SERVERS', default=None))
    setting_value('CACHE_MEMCACHED_USERNAME', env('MEMCACHIER_USERNAME', default=None))
    setting_value('CACHE_MEMCACHED_PASSWORD', env('MEMCACHIER_PASSWORD', default=None))
