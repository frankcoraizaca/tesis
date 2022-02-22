from .base import *
import os
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbempledo',
        'USER': 'ventiepn',
        'PASSWORD': '19951992',
        'HOST': 'localhost',
        'PORT': '5432',

    }
}
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-file
STATIC_URL = '/static/'

STATIC_DIR=os.path.join(BASE_DIR,"static")
STATICFILES_DIRS = [STATIC_DIR,]




# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
