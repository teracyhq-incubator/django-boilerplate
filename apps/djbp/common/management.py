"""
Update the default Site object basing on the settings
"""

from django.apps import apps
from django.conf import settings
from django.db import DEFAULT_DB_ALIAS, router


def update_default_site(app_config, verbosity=2, interactive=True, using=DEFAULT_DB_ALIAS,
                        **kwargs):
    try:
        Site = apps.get_model('sites', 'Site')
    except LookupError:
        return

    if not router.allow_migrate_model(using, Site):
        return

    if verbosity >= 2:
        print('Updating example.com Site object')

    if getattr(settings, 'SITE_ID', None):
        site = Site.objects.get(pk=settings.SITE_ID)
        site.domain = settings.SITE_DOMAIN
        site.name = settings.SITE_NAME
        site.save(using=using)
