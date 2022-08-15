from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Template, UserTemplate, User
from django.core.serializers import serialize
import json


def templates(request):
    templates = Template.objects.all()
    return render(request, 'template.html', {"templates":templates})


def addTemplate(request):
    return render(request, 'newtemplate.html')


def saveTemplate(request):
    if(request.method=='POST'):
        html = request.POST['html']
        css = request.POST['css']
        usertemplate = UserTemplate.objects.create(
            name='untitled', 
            html=html, 
            css=css,
            created_by = request.user
        )
        usertemplate.save()
    #return JsonResponse({ "result" : (json.loads(serialize('json', [usertemplate])))[0]})
    return redirect('home')


def editTemplate(request, id):
    template = Template.objects.get(pk=id)
    return render(request, 'newtemplate.html', {"template":template})


def editTemplateContent(request, id):
    if(request.method=='POST'):
        html = request.POST['html']
        css = request.POST['css']
        usertemplate = UserTemplate.objects.create(
            name='untitled', 
            html=html, 
            css=css,
            created_by = request.user
        )
        usertemplate.save()
    #return JsonResponse({ "result" : (json.loads(serialize('json', [usertemplate])))[0]})
    return redirect('home')


def previewTemplate(request, id):
    usertemplate = UserTemplate.objects.get(pk=id)
    return render(request, 'preview.html', {"usertemplate":usertemplate})


def addusertemplate(request):
    return render(request, 'new_user_template.html')


def edit_userTemplates(request, id):
    usertemplate = UserTemplate.objects.get(pk=id)
    return render(request, 'new_user_template.html', {"usertemplate":usertemplate})

#issue is coming from here
def edit_userTemplateContent(request, id):
    if(request.method=='POST'):
        html = request.POST['html']
        css = request.POST['css']
        usertemplate = UserTemplate.objects.get(pk=id)
        usertemplate.html = html
        usertemplate.css = css
        usertemplate.save()
    return JsonResponse({ "result" : (json.loads(serialize('json', [usertemplate])))[0]})

def saveUserTemplate(request):
    if(request.method=='POST'):
        html = request.POST['html']
        css = request.POST['css']
        usertemplate = UserTemplate.objects.create(
            name="untitled", 
            html=html, 
            css=css,
            created_by = request.user
        )
        usertemplate.save()
    return JsonResponse({ "result" : (json.loads(serialize('json', [usertemplate])))[0]})


def add_allTemplate(request):
    return render(request, 'new_all_template.html')


def save_allTemplate(request):
    if(request.method=='POST'):
        html = request.POST['html']
        css = request.POST['css']
        template = Template.objects.create(name='untitled', html=html, css=css)
        template.save()
    return JsonResponse({ "result" : (json.loads(serialize('json', [template])))[0]})
