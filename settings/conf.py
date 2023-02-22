from pathlib import Path
import os
import sys


# Standart settings

BASE_DIR = Path(__file__).resolve().parent.parent

sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, 'apps'))

SECRET_KEY = 'django-insecure-i#1xq_(vxtsoz3vfril74o6%n65$b9_5=tdq=@dgmvcx*6%m$k'

DEBUG = True

ALLOWED_HOSTS = ["*"]

WSGI_APPLICATION = 'settings.wsgi.application'

ROOT_URLCONF = 'settings.urls'

# Datatime and language

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Static

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# DRF

# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
#     ]
# }

# TOOLBAR

INTERNAL_IPS = [
    "127.0.0.1",
]
