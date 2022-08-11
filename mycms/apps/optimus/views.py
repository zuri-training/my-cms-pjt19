from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Portfolio
from django.core.serializers import serialize
import json

# Create your views here.
def index(request):
    portfolio = Portfolio.objects.all()
    return render(request, 'honeylens.html', 'IRONHIDE.html', {"porfolio": portfolio})

def addPortfolio(request):
    render(request, 'honeylens.html', 'IRONHIDE.html')

def savePortfolio(request):
    if(request.method =='POST'):
        html = request.POST['html']
        css = request.POST['css']
        portfolio = Portfolio.objects.create(names="untitled", html=html, css=css)
        portfolio.save()
    return JsonResponse[{ "result" : [json.loads(serialize('json', [portfolio]))][0]}]

def editPortfolio(request, id):
    portfolio = Portfolio.objects.get(pk=id)
    return render(request, 'honeylens.html', 'IRONHIDE.html', {"portfolio": portfolio})

def editPortfolioContent(request, id):
    if(request.method =='POST'):
        html = request.POST['html']
        css = request.POST['css']
        portfolio = Portfolio.objects.get(pk=id)
        portfolio.html = html
        portfolio.css = css
        portfolio.save()
    return JsonResponse[{ "result" : [json.loads(serialize('json', [portfolio]))][0]}]


