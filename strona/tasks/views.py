from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.shortcuts import redirect

def index(request):
    return render(request, 'tasks/home.html')

def home(request):
    return render(request, 'tasks/home.html')

def oNas(request):
    return render(request, 'tasks/oNas.html')

def oProjekcie(request):
    return render(request, 'tasks/oProjekcie.html')

def kontakt(request):
    return render(request, 'tasks/kontakt.html')

def dokumenty(request):
    return render(request, 'tasks/dokumenty.html')

def spotkania(request):
    return render(request, 'tasks/spotkania.html')

def galeria(request):
    return render(request, 'tasks/galeria.html')





