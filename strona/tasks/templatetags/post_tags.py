from django.shortcuts import render
from django.http import HttpResponse
from django import template
from ..models import *

register = template.Library()

@register.simple_tag

def pierwsze():
    return Wlosy.objects.get(id=1)

@register.simple_tag

def drugie():
    return Wstep.objects.latest('imie') 