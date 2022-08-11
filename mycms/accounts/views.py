from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm

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
      login(request, user)
      return redirect('home')
  else: 
    form = RegisterForm()

  return(render(request, 'registration/signup.html', {"form": form}))

# @login_required
def home(request):
  return render(request, 'allTemplates.html')

def portfolio(request):
  return render(request, 'portfolio.html')