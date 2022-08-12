from django.urls import path, include
from .  import views

urlpatterns = [
  path('', views.index, name= 'index'),
  path('index', views.index, name= 'index'),
  path('sign-up', views.signup, name= 'signup'),
  path('home', views.home, name= 'home'),
  path('about', views.about, name= 'about'),
  path('home/portfolio', views.portfolio, name= 'portfolio'),
  path('home/landingpages', views.landingpages, name= 'landingpages'),
  path('home/blogs', views.blogs, name= 'blogs'),
  path('home/support', views.support, name= 'support'),
]