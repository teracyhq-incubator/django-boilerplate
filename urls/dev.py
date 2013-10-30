"""
settings for urls in developing mode
"""

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from urls.common import *  # noqa

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns += (
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
