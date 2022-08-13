from django.contrib import admin
from .models import Template, UserTemplate

# Register your models here.
admin.site.register(Template)
admin.site.register(UserTemplate)