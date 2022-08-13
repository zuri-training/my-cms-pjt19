from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Template, UserTemplate, User
from django.core.serializers import serialize
import json

# def index(request):
#     templates = Template.objects.all()
#     return render(request, 'optimus.html')


def templates(request):
    templates = Template.objects.all()
    return render(request, 'template.html', {"templates":templates})


def addTemplate(request):
    return render(request, 'newtemplate.html')


def saveTemplate(request):
    if(request.method=='POST'):
        html = request.POST['html']
        css = request.POST['css']
        #template = Template.objects.create(name='untitled', html=html, css=css)
        usertemplate = UserTemplate.objects.create(
            name='untitled', 
            html=html, 
            css=css,
            created_by = request.user
        )
        #template.save()
        usertemplate.save()
    return JsonResponse({ "result" : (json.loads(serialize('json', [usertemplate])))[0]})


def editTemplate(request, id):
    template = Template.objects.get(pk=id)
    return render(request, 'newtemplate.html', {"template":template})


def editTemplateContent(request, id):
    if(request.method=='POST'):
        html = request.POST['html']
        css = request.POST['css']
        template = Template.objects.get(pk=id)
        usertemplate = UserTemplate.objects.create(
            name='untitled', 
            html=html, 
            css=css,
            created_by = request.user
        )
        usertemplate.save()
        #template.save()
    return JsonResponse({ "result" : (json.loads(serialize('json', [usertemplate])))[0]})


def previewTemplate(request, id):
    usertemplate = UserTemplate.objects.get(pk=id)
    return render(request, 'preview.html', {"usertemplate":usertemplate})


def userTemplates(request, name):
    user = User.objects.all(user=request.user)
    usertemplates = UserTemplate.objects.all().filter(created_by=user)
    return render(request, 'user_templates.html', {"usertemplates":usertemplates})

def edit_userTemplates(request, id):
    usertemplate = UserTemplate.objects.get(pk=id)
    return render(request, 'new_user_template.html', {"usertemplate":usertemplate})

def edit_userTemplateContent(request, id):
    #user = User.objects.get(user=request.user)
    if(request.method=='POST'):
        html = request.POST['html']
        css = request.POST['css']
        usertemplate = UserTemplate.objects.get(pk=id)
        # usertemplate.name='untitled' 
        usertemplate.html = html
        usertemplate.css = css
        # usertemplate.created_by = request.user
        usertemplate.save()
    return JsonResponse({ "result" : (json.loads(serialize('json', [usertemplate])))[0]})

def saveUserTemplate(request, id):
    if(request.method=='POST'):
        html = request.POST['html']
        css = request.POST['css']
        #template = Template.objects.create(name='untitled', html=html, css=css)
        usertemplate = UserTemplate.objects.get(pk=id) 
        usertemplate.html=html
        usertemplate.css=css      
        #template.save()
        usertemplate.save()
    return JsonResponse({ "result" : (json.loads(serialize('json', [usertemplate])))[0]})

    