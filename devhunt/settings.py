"""
Django settings for devhunt project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

from __future__ import unicode_literals

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from spirit.settings import *

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/


# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']

ROOT_URLCONF = 'devhunt.urls'

WSGI_APPLICATION = 'devhunt.wsgi.application'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

INSTALLED_APPS += (
    'landing',
    'django_gravatar',
)

try:
    from .local_settings import *
except ImportError:
    pass

try:
    from .production_settings import *
except ImportError:
    pass
