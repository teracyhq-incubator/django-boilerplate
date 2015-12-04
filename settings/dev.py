"""
settings for development mode
"""
from .project.common import *  # noqa

DATA_DIR = os.path.join(PROJECT_DIR, 'data')

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ROOT_URLCONF = os.environ.get('ROOT_URLCONF', 'urls.project.dev')

EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND', 'django.core.mail.backends.console.EmailBackend')

INTERNAL_IPS = ('10.0.2.2', '127.0.0.1', '0.0.0.0')

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)


INSTALLED_APPS += (
    'django.contrib.admin',
    'debug_toolbar',
    'django_nose',
)

# Use nose to run all tests
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
