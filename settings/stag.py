"""
settings for staging mode
"""
from project.settings.common import *  # noqa

DEBUG = False

ROOT_URLCONF = os.environ.get('ROOT_URLCONF', 'project.urls.stag')
