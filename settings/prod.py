# settings for production
from default import *

#heroku
# Parse database configuration from $DATABASE_URL
if environ.has_key('DATABASE_URL'):
    import dj_database_url
    DATABASES['default'] = dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')