"""
Settings for the live server. Used by wsgi.py / asgi.py. NOT for your PC.
Stage 10 tightens these further; this is the safe starting point.
"""
import os

from django.core.exceptions import ImproperlyConfigured

from .base import *  # noqa: F401,F403
from .base import ALLOWED_HOSTS

DEBUG = False

if not ALLOWED_HOSTS:
    raise ImproperlyConfigured("Set ALLOWED_HOSTS in the server's environment (.env).")

CSRF_TRUSTED_ORIGINS = [o.strip() for o in os.environ.get('CSRF_TRUSTED_ORIGINS', '').split(',') if o.strip()]

# HTTPS and cookie protection
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')  # only if the server sits behind a proxy that sets this
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 3600   # raise to 31536000 (1 year) once HTTPS is confirmed working
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_REFERRER_POLICY = 'same-origin'
X_FRAME_OPTIONS = 'DENY'