"""
Django settings for Geodjango project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
import socket
import docker_config
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
with open('secret_key.txt') as f:
    SECRET_KEY = f.read().strip()
    #SECRET_KEY = '+rlerwq4l)lmn^z&n$5vhj&w+8ub&295696b_qa4t1(m0yzl+z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'crispy_forms',
    'leaflet',
    'world',
]

MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Geodjango.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR.joinpath('templates'))],  # 'DIRS': [BASE_DIR / 'templates']
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

WSGI_APPLICATION = 'Geodjango.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'gis',
        'HOST': 'database_contain',  # 'HOST': 'localhost' / database_contain
        'USER': 'docker',
        'PASSWORD': 'docker',
        'PORT': 5432,  # 'PORT': 25432 / 5432
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


CRISPY_TEMPLATE_PACK = 'bootstrap4'
CRISPY_FAIL_SILENTLY = not DEBUG

LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (53.0, -8.0),
    'DEFAULT_ZOOM': 6,
    'MIN_ZOOM': 3,
    'MAX_ZOOM': 18,
    'RESET_VIEW': False,
    'SCALE': None,
    'OPACITY': 0.5,
}

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# whitenoise lab 4
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Need to comment out this section for local use
if socket.gethostname() =="LAPTOP-33PIMB4L":
    DATABASES["default"]["HOST"] = "localhost"
    DATABASES["default"]["PORT"] = docker_config.POSTGIS_PORT
else:
    DATABASES["default"]["HOST"] = f"{docker_config.PROJECT_NAME}-postgis"
    DATABASES["default"]["PORT"] = 5432

# Set DEPLOY_SECURE to True only for LIVE deployment
if docker_config.DEPLOY_SECURE:
    DEBUG = False
    TEMPLATES[0]["OPTIONS"]["debug"] = False
    ALLOWED_HOSTS = ['.killianpogue.xyz', 'localhost', '172.31.44.190']
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
else:
    DEBUG = True
    TEMPLATES[0]["OPTIONS"]["debug"] = True
    ALLOWED_HOSTS = ['*', ]
    CSRF_COOKIE_SECURE = False
    SESSION_COOKIE_SECURE = False





# LOGIN_REDIRECT_URL = redirect the user to this url
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'
