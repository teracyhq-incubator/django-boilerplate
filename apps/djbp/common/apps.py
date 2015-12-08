from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.utils.translation import ugettext_lazy as _

from .management import update_default_site


class CommonConfig(AppConfig):
    name = 'djbp.common'
    verbose_name = _('django-boilerplate-common')

    def ready(self):
        post_migrate.connect(update_default_site, sender=self)
