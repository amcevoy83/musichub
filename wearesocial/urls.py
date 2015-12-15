"""wearesocial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
import core
from django.conf.urls.static import static
import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/subscriptions/$', 'accounts.views.subscriptions_webhook', name='subscriptions'),
    url(r'^$', 'core.views.get_index', name='home'),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^contact/', 'contact.views.contact', name='contact'),
    url(r'^register/$','accounts.views.register', name='register'),
    url(r'^login/$','accounts.views.login', name='login'),
    url(r'^logout/$','accounts.views.logout', name='logout'), ##removed two // at the start of the logout regex
    url(r'^profile/$', 'accounts.views.profile', name='profile'),
]+ static(settings.MEDIA_URL, dcument_root= settings.MEDIA_ROOT)
+ static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
