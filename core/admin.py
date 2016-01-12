from django.contrib import admin
from contact.models import ContactForm
from threads.models import Subject, Thread, Posts

# Register your models here.
admin.site.register(ContactForm)
admin.site.register(Posts)
admin.site.register(Thread)
admin.site.register(Subject)