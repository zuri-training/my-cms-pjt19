from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import (
  AbstractBaseUser,
  PermissionsMixin
)

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
  name = models.CharField(max_length = 240)
  email = models.EmailField(max_length = 255, unique=True)
  mobile = models.CharField(max_length = 50)
  password1 = models.CharField(max_length = 240)

  is_staff = models.BooleanField(default=True)
  is_active = models.BooleanField(default=True)
  is_superuser = models.BooleanField(default=False)

  objects = CustomUserManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['name','mobile','password1', 'password2']
  
  class Meta:
    ordering = ['email']
    verbose_name = 'User'
    verbose_name_plural = 'Users'
    
  def __str__(self):
    return self.email