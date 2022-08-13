from email.policy import default
from django.db import models
from accounts.models import User

# Create your models here.
class Template(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    html = models.TextField()
    css = models.TextField()
    thumbnails = models.ImageField(default="https://tailwindui.com/img/ecommerce-images/home-page-02-edition-01.jpg")

class UserTemplate(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    html = models.TextField()
    css = models.TextField()
    thumbnails = models.ImageField(null=True, blank=True, default="none")
    created_by = models.ForeignKey(User, related_name='usertemplates', on_delete=models.DO_NOTHING)
    parent_template = models.ForeignKey(Template, related_name='usertemplates', on_delete=models.CASCADE, null=True, blank=True)