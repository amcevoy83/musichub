from settings import BASE_DIR, INSTALLED_APPS, os

DEBUG = True

INSTALLED_APPS += (
    'debug_toolbar',

)

TEMPLATE_DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_ROOT = ''