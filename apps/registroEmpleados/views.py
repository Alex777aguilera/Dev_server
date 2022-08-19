from ast import For
from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .models import *


def index(request):
    context = {'xd': 'index'}
    html_template = loader.get_template('index.html')
    
    
    return HttpResponse(html_template.render(context, request))

def datos(request):
    users = User.objects.all()
    ctx = {'users':users}
    return render(request, 'datos.html',ctx)

def info(request):
    
    
    return render(request, 'info.html')
