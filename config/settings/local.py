# -*- coding: utf-8 -*-
import os
import socket

from .common import *  # noqa

# DEBUG
# ------------------------------------------------------------------------------
DEBUG = env.bool('DJANGO_DEBUG', default=True)
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default='3(!oafihrr4deyrh5=vs_sr*8@f-vo=tyq)qnc8lys3pldb2*)')

# ALLOWED HOSTS
# ------------------------------------------------------------------------------
ALLOWED_HOSTS = ['192.168.99.100', 'localhost']

# Mail settings
# ------------------------------------------------------------------------------

EMAIL_PORT = 1025
EMAIL_HOST = 'localhost'
EMAIL_BACKEND = env(
    'DJANGO_EMAIL_BACKEND',
    default='django.core.mail.backends.console.EmailBackend')

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_app',
        'USER': 'postgres' if env('TRAVIS_CI', default=False) else 'db_user',
        'PASSWORD': 'db_pass',
        'HOST': 'db' if env('INSIDE_DOCKER', default=False) else 'localhost',
        'PORT': 5432,
    }
}

# CACHING
# ------------------------------------------------------------------------------
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

# django-debug-toolbar
# ------------------------------------------------------------------------------
MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware', )
INSTALLED_APPS += ('debug_toolbar', )

INTERNAL_IPS = [
    '127.0.0.1',
    '10.0.2.2',
    '192.168.99.100',
]

# Fix django-debug-toolbar when running Django in a Docker container
if env('INSIDE_DOCKER', default=False):
    ip = socket.gethostbyname(socket.gethostname())
    INTERNAL_IPS += [ip[:-1] + "1"]

DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}

# Additional local apps
# ------------------------------------------------------------------------------
INSTALLED_APPS += ('django_extensions', 'rosetta', 'stdimage_serializer')

# TESTING
# ------------------------------------------------------------------------------
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# Your local stuff: Below this line define 3rd party library settings
ROSETTA_ENABLE_TRANSLATION_SUGGESTIONS = True
