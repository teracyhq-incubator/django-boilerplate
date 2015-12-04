"""
settings for staging mode
"""
from .project.common import *  # noqa

DEBUG = False

ROOT_URLCONF = os.environ.get('ROOT_URLCONF', 'urls.project.stag')
