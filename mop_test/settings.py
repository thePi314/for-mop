"""
Django settings for mop_test project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import environ
import os

env = environ.Env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
ROOT_DIR = environ.Path(__file__) - 2


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('SECRET_KEY', default='')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'drf_yasg',
    'rest_framework',
    'django_celery_beat',
    'channels',
    'api.apps.ApiConfig',
    'scraper.apps.ScraperConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

if DEBUG:
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
    INSTALLED_APPS += ['debug_toolbar']

    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': lambda _request: DEBUG
    }

ROOT_URLCONF = 'mop_test.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mop_test.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env.str('POSTGRES_DB'),
        'USER': env.str('POSTGRES_USER'),
        'PASSWORD': env.str('POSTGRES_PASSWORD'),
        'HOST': env.str('POSTGRES_HOST'),
        'PORT': env.str('POSTGRES_PORT'),
    },
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/


STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATIC_URL = '/static/'

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'api.utils.error_handler.custom_exception_handler',
    'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.SessionAuthentication']
}

REDIS_HOST = env.str('REDIS_HOST', 'redis')
REDIS_PORT = env.str('REDIS_PORT', '6379')
REDIS_SLOT = env.str('REDIS_SLOT', '0')
REDIS_PASSWORD = env.str('REDIS_PASSWORD', None)
REDIS_USER = env.str('REDIS_USER', None)
REDIS_CLUSTER = env.bool('REDIS_CLUSTER', False)

if REDIS_USER:
    REDIS_USER = REDIS_USER + '@'
else:
    REDIS_USER = ''
REDIS_CHANNELS_SLOT = env.str('REDIS_CHANNELS_SLOT', '1')

REDIS_URL = f'redis://{REDIS_USER}{REDIS_HOST}:{REDIS_PORT}/{REDIS_SLOT}'

REDIS_OPTIONS = {
    'PASSWORD': REDIS_PASSWORD
}

if REDIS_CLUSTER:
    REDIS_OPTIONS['CLIENT_CLASS'] = "api.util.redis.ClusterRedisClient"

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': [REDIS_URL],
        'OPTIONS': REDIS_OPTIONS
    },
}

if REDIS_PASSWORD:
    REDIS_PASSWORD = ':' + REDIS_PASSWORD + '@'
    REDIS_USER = env.str('REDIS_USER', '')
else:
    REDIS_PASSWORD = ''

CELERY_BROKER_URL = f"amqp://{env.str('RABBITMQ_USER')}:{env.str('RABBITMQ_PASSWORD')}@{env.str('RABBITMQ_HOST')}:{env.str('RABBITMQ_PORT')}/{env.str('RABBITMQ_VHOST')}"
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [f'redis://{REDIS_USER}{REDIS_PASSWORD}{REDIS_HOST}:{REDIS_PORT}/{REDIS_CHANNELS_SLOT}'],
        },
    },
}

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'