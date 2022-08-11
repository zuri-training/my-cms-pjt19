from django.urls import path, include
from .  import views

urlpatterns = [
  path('', views.index, name= 'index'),
  path('index', views.index, name= 'index'),
  path('sign-up', views.signup, name= 'signup'),
  path('home', views.home, name= 'home'),
  path('home/portfolio', views.portfolio, name= 'portfolio'),
]