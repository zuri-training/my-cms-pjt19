from django.urls import path
from . import views

urlpattern = [
    path('', views.index, name='index'),
    path('add', views.addPortfolio, name="addporfolio"),
    path('edit/<id>', views.editPortfolio, name="editportfolio"),
    path('portfolio/create', views.savePortfolio, name="create_posrtfolio"),
    path('editportfolio/<id>', views.editPortfolioContent, name="editPortfolioContent")    
]