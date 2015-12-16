"""
Django settings for wearesocial project.

Generated by 'django-admin startproject' using Django 1.8.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import django.contrib.staticfiles


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^n68uy760rq364hpl3h4tkc^3$!w1p$ur#d@13gc(0+om=7uix'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

SITE_ID = 1
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'core',
    'contact',
    'accounts',
    'django_forms_bootstrap',
    'django_static_jquery',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
     'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'
)

ROOT_URLCONF = 'wearesocial.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'wearesocial.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'testdb',
        'USER': 'testuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT':'5432'
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)  #add a directory at the project level

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, "static"),

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR,'media' )

AUTH_USER_MODEL = 'accounts.User'

AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend','accounts.backends.EmailAuth',)

EMAIL_HOST_USER = 'aoifemcevoy@gmail.com'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_PASSWORD = 'fm5g53mh!'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISABLE', 'pk_test_Qv9Y4s1Ob24xrPAAhlUdg0sy')

STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_rP1gTjriAoHxeX4nygRs44dh')

TEMPLATE_DEBUG = False

LOGGING = {
    'version': 1,
}

try:
    from local_settings import *
except:
    pass
