SECRET_KEY = 'random_for_travis'

DEBUG = False
TEMPLATE_DEBUG = False

STATIC_ROOT = 'website/static'
MEDIA_ROOT = 'website/media'

EMAIL_HOST_USER = 'claremont_academia@yahoo.com'
EMAIL_HOST_PASSWORD = 'RANDOM'

from website.configuration import *