from django.contrib import admin
from contact.models import ContactForm
from core.models import Register

# Register your models here.
admin.site.register(ContactForm)
admin.site.register(Register)