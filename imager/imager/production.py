from settings import *
import os

DEBUG = False
TEMPLATE_DEBUG = False
THUMBNAIL_DEBUG = False
ALLOWED_HOSTS = ['*']
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
