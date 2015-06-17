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

ALLOWED_HOSTS = ['127.0.0.1','localhost']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'django_mobile',
    'pysolr',
    'haystack',
    'geoposition',
    'widget_tweaks',
    'autocomplete_light',
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
    'django_mobile.middleware.MobileDetectionMiddleware',
    'django_mobile.middleware.SetFlavourMiddleware',
)

ROOT_URLCONF = 'website.urls'

WSGI_APPLICATION = 'website.wsgi.application'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django_mobile.context_processors.flavour',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django_mobile.loader.Loader',
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



ENV_PATH = os.path.abspath(os.path.dirname(__file__))
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(ENV_PATH, 'static/')
MEDIA_ROOT = os.path.join(ENV_PATH, 'media/')
MEDIA_URL = "/media/"

PROJECT_PATH = os.path.join(ENV_PATH, os.pardir)

STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'workflow', 'static'),
    os.path.join(PROJECT_PATH, 'mainsite', 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATIC_ROOT = os.path.join(ENV_PATH, 'static')


LOGIN_URL = '/workflow/login'

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://127.0.0.1:8983/solr'
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

# Only for development
EMAIL_USE_TLS = True
EMAIL_HOST = "smtp.mail.yahoo.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = 'claremont_academia@yahoo.com'
EMAIL_HOST_PASSWORD = '794613852'
DEFAULT_FROM_EMAIL = 'claremont_academia@yahoo.com'

GEOPOSITION_MAP_WIDGET_HEIGHT = 240
