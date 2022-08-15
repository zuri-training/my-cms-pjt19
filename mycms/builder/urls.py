from django.urls import path
from . import views

urlpatterns = [
    path('templates/', views.templates, name="templates"),
    path('add', views.addTemplate, name="addtemplate"),
    path('edit/<id>', views.editTemplate, name="editTemplate"),
    path('template/create', views.saveTemplate, name="create_template"),
    path('editTemplate/<id>', views.editTemplateContent, name="editTemplateContent"),
    path('preview/<id>', views.previewTemplate, name="previewtemplate"),
    path('addnewtemplate', views.addusertemplate, name="addusertemplate"),
    path('editMyTemplate/<id>', views.edit_userTemplates, name="edit_userTemplates"),
    path('editMyTemplateContent/<id>', views.edit_userTemplateContent, name="edit_userTemplateContent"),
    path('userTemplate/create', views.saveUserTemplate, name="create_user_template"),
    path('add_allTemplate', views.add_allTemplate, name="add_alltemplate"),
    path('alltemplate/create', views.save_allTemplate, name="create_alltemplate"),
]
