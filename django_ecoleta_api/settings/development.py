from .base import *

ALLOWED_HOSTS += ['127.0.0.1']
DEBUG = True

WSGI_APPLICATION = 'django_ecoleta_api.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ecoleta',
        'USER': 'igor',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': ''
    }
}

CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',
)
