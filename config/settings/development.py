"""Settings for working on your own PC. Used by manage.py.""" 
import os 
 
from .base import *  # noqa: F401,F403 
from .base import ALLOWED_HOSTS as _HOSTS 
 
DEBUG = os.environ.get('DEBUG', 'True') == 'True' 
ALLOWED_HOSTS = _HOSTS or ['127.0.0.1', 'localhost'] 
 
# Emails (such as login codes) are printed in this window instead of being sent. 
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' 
