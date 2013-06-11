# settings for development
from common import *

INTERNAL_IPS = ('127.0.0.1',)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)


STATICFILES_FINDERS += (
    'compressor.finders.CompressorFinder',
)

INSTALLED_APPS += (
    'django.contrib.admin',
    'debug_toolbar',
    'compressor',
    'teracy.html5boilerplate',
)