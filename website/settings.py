"""
Django settings for website project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5k40^z0@#$*9oj%cndadvu#a_-6@keu+9(#wi&ty1x4dsshy=1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'pysolr',
    'haystack',
    'ajax_select',
    'widget_tweaks',
    'mainsite',
    'workflow',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'website.urls'

WSGI_APPLICATION = 'website.wsgi.application'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
)

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

ENV_PATH = os.path.abspath(os.path.dirname(__file__))
MEDIA_ROOT = os.path.join(ENV_PATH, 'media/')

PROJECT_PATH = os.path.join(ENV_PATH, os.pardir)

STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'workflow', 'static'),
    os.path.join(PROJECT_PATH, 'mainsite', 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

STATIC_ROOT = os.path.join(ENV_PATH, 'static')


LOGIN_URL = '/workflow/login'

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://127.0.0.1:8983/solr'
        # ...or for multicore...
        # 'URL': 'http://127.0.0.1:8983/solr/mysite',
    },
}

from django.conf import settings
# Specify the selenium test runner
SELENIUM_TEST_RUNNER = getattr(settings, 'SELENIUM_TEST_RUNNER',
                               'django_selenium.selenium_runner.SeleniumTestRunner')

SELENIUM_TIMEOUT = getattr(settings, 'SELENIUM_TIMEOUT', 120)
SELENIUM_DRIVER_TIMEOUT = getattr(settings, 'SELENIUM_DRIVER_TIMEOUT', 10)
# Specify max waiting time for server to finish processing request and deactivates
SELENIUM_TEST_SERVER_TIMEOUT = getattr(settings, 'SELENIUM_TEST_SERVER_TIMEOUT', 300)
SELENIUM_TESTSERVER_HOST = getattr(settings, 'SELENIUM_TESTSERVER_HOST', 'localhost')
SELENIUM_TESTSERVER_PORT = getattr(settings, 'SELENIUM_TESTSERVER_PORT', 8011)
SELENIUM_HOST = getattr(settings, 'SELENIUM_HOST', None)
SELENIUM_PORT = getattr(settings, 'SELENIUM_PORT', 4444)
SELENIUM_DISPLAY = getattr(settings, 'SELENIUM_DISPLAY', ':0')
# Set the drivers that you want to run your tests against
SELENIUM_DRIVER = getattr(settings, 'SELENIUM_DRIVER', 'Firefox')
SELENIUM_DRIVER_OPTS = getattr(settings, 'SELENIUM_DRIVER_OPTS', dict())

AJAX_LOOKUP_CHANNELS = {
    'profile' : ('workflow.lookups','ProfileLookup')
}