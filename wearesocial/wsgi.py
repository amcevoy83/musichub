"""
WSGI config for wearesocial project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""
##-----------------ORIGINAL CODE  ---------------------
import os
import django
django.setup()
from django.core.wsgi import get_wsgi_application

os.environ.setdefault["DJANGO_SETTINGS_MODULE"]= "wearesocial.settings"

#settings.configure()

application = get_wsgi_application()
##-----------------ORIGINAL CODE  ---------------------
