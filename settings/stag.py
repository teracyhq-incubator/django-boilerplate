"""
settings for staging mode
"""
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS  # noqa
from .project.common import *  # noqa

ROOT_URLCONF = 'urls.project.stag'
