"""
Settings shared by every environment (your PC and the live server).

Environment-specific settings live next to this file:
    development.py  -> used on your PC (manage.py)
    production.py   -> used on the live server (wsgi.py / asgi.py)

Secrets are NEVER written here. They come from the ".env" file.
"""
import os
from pathlib import Path

from dotenv import load_dotenv

# config/settings/base.py -> project root is three folders up
BASE_DIR = Path(__file__).resolve().parent.parent.parent
load_dotenv(BASE_DIR / '.env')

# --- Secrets and hosts (from .env) -------------------------------------
SECRET_KEY = os.environ['SECRET_KEY']  # stops with a clear error if missing
DEBUG = False  # switched on only in development.py
ALLOWED_HOSTS = [h.strip() for h in os.environ.get('ALLOWED_HOSTS', '').split(',') if h.strip()]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --- Applications ------------------------------------------------------
INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'marketplace',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# --- Database (PostgreSQL, credentials from .env) ----------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}

# --- Password rules ----------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --- Language and time -------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Lusaka'   # times are stored in UTC and shown in Zambian time
USE_I18N = True
USE_TZ = True

# --- Static files (our own css/js/img) and uploaded media --------------
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']      # our own files
STATIC_ROOT = BASE_DIR / 'staticfiles'        # filled by "collectstatic", never edited by hand

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# --- Login -------------------------------------------------------------
LOGIN_URL = '/'

# --- Jazzmin admin look ------------------------------------------------
JAZZMIN_SETTINGS = {
    "site_title": "KurtonBerg Admin",
    "site_header": "KurtonBerg Agency",
    "site_brand": "KurtonBerg Admin",
    "welcome_sign": "Welcome to KurtonBerg Management Dashboard",
    "copyright": "KurtonBerg Agency Zambia",
    "search_model": ["marketplace.Car", "marketplace.Property"],
    "top_menu_links": [
        {"name": "← Back to Marketplace", "url": "marketplace_home", "permissions": ["auth.view_user"]},
        {"model": "marketplace.Car"},
        {"model": "marketplace.Property"},
    ],
    "user_avatar": "admin_profile.profile_picture",
    "show_sidebar": True,
    "navigation_expanded": True,
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "marketplace.car": "fas fa-car",
        "marketplace.property": "fas fa-building",
        "marketplace.cart": "fas fa-shopping-cart",
        "marketplace.enquiry": "fas fa-envelope",
        "marketplace.favorite": "fas fa-heart",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    "related_modal_active": True,
}

JAZZMIN_UI_TWEAKS = {
    "theme": "flatly",
    "dark_mode_theme": "solar",
}