from django.db import models
from tinymce.models import HTMLField
from django.utils import timezone
from musichub.musichub import settings


class Subject(models.Model):
    name = models.CharField(max_length=254)
    description = HTMLField()

    def __unicode__(self):
        return self.name

class Thread(models.Model):
    name = models.CharField(max_length=254)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='threads')
    subject = models.ForeignKey(Subject,related_name='threads')
    created_at = models.DateField(default=timezone.now)

class Posts(models.Model):
    thread = models.ForeignKey(Thread, related_name='posts')
    comment = HTMLField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts')
    created_at = models.DateTimeField(default=timezone.now)
