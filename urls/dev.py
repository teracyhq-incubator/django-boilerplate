from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from common import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns += (
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()