#-*- coding: utf-8 -*-
# Copyright (C) 1998-2012 by the Free Software Foundation, Inc.
#
# This file is part of Postorius.
#
# Postorius is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# Postorius is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# Postorius.  If not, see <http://www.gnu.org/licenses/>.

import os
import sys

"""Django settings for postorius project."""

import os.path

# Mailman API credentials for testing
MAILMAN_API_URL = 'http://localhost:9001'
MAILMAN_USER = 'restadmin'
MAILMAN_PASS = 'restpass'

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = ('localhost', )

ADMINS = (
    #('Admin', 'webmaster@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_PATH,'postorius.db')
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds static files.
STATIC_ROOT = os.path.join(PROJECT_PATH, 'static/')
# Absolute path to the directory that holds media files.
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media/')
# URL that handles the media served from STATIC_ROOT. Make sure to use a
STATIC_URL = '/static/'
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '$!-7^wl#wiifjbh)5@f7ji%x!vp7s1vzbvwt26hxv$idixq0u0'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'django_browserid.auth.BrowserIDBackend',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.csrf",
    "django.contrib.messages.context_processors.messages",
    "postorius.context_processors.postorius",
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
)

# Set `postorius.urls` as main url config if postorius
# is the only app you want to serve.
ROOT_URLCONF = 'postorius.urls'

TEMPLATE_DIRS = (
    # uncomment if you like to overwrite the default templates:
    # os.path.join(PROJECT_PATH, "/templates/postorius"),
)

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.messages',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'postorius',
    'django_browserid',
    # These are only used for development
    # 'debug_toolbar',
)
LOGIN_URL          = '/postorius/accounts/login/'
LOGIN_REDIRECT_URL = '/postorius/'
LOGIN_ERROR_URL    = '/postorius/accounts/login/'

def username(email):
    return email.rsplit('@', 1)[0]
BROWSERID_USERNAME_ALGO = username


# Set VCR_RECORD_MODE to 'all' to re-record all API responses.
# (Remember to use an empty mailman database!)
VCR_RECORD_MODE = 'once'
