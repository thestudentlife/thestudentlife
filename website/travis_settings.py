from website.settings_shared import *

SECRET_KEY = 'random_for_travis'

DEBUG = False
TEMPLATE_DEBUG = False

STATIC_ROOT = os.path.join(ENV_PATH, 'static')
MEDIA_ROOT = os.path.join(ENV_PATH, 'media')

EMAIL_HOST_USER = 'claremont_academia@yahoo.com'
EMAIL_HOST_PASSWORD = 'random_for_travis'

DROPBOX_CLIENT_ID = ''