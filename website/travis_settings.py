SECRET_KEY = 'random_for_travis'

DEBUG = False
TEMPLATE_DEBUG = False

STATIC_ROOT = 'website/static'
MEDIA_ROOT = 'website/media'

from website.configuration import *