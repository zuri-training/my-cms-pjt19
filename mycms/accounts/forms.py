from .models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class RegisterForm(UserCreationForm):
  class Meta:
    model = User
    fields = [
      "email",
      'name',
      'mobile',
      'password1',
      'password2'
    ]
  
  
class CustomUserChangeForm(UserChangeForm):
  class Meta:
    model = User
    fields = ["email"]