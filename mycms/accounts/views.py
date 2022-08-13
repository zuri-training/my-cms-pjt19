from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm
from .models import User
from builder.models import UserTemplate

from django.views.decorators.csrf import csrf_protect 



# Create your views here.
def index(request):
  return render(request,'index.html')

@csrf_protect
def signup(request):
  if request.method == "POST":
    form = RegisterForm(request.POST)
    if form.is_valid():
      user = form.save()
      # username = form.cleaned_data.get('email')
      # raw_password = form.cleaned_data.get('password')
      # user = authenticate(username=username, password=raw_password)
      login(request, user)
      return redirect('home')
  else: 
    form = RegisterForm()

  return(render(request, 'registration/signup.html', {"form": form}))

  #@login_required
def home(request):
    #user = User.objects.get(name=request.user)
    usertemplates = UserTemplate.objects.all().filter(created_by=request.user)
    return render(request, 'user_templates.html', {"usertemplates":usertemplates})

def logout_user(request):
    logout(request)
    return redirect('index')