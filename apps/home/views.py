from django.shortcuts import render

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.core.mail import EmailMessage, send_mail
from config.settings import EMAIL_HOST_USER


def index(request):
    context = {'xd': 'index'}
    v = False
    html_template = loader.get_template('index.html')
    if request.method == 'POST':
        v = Send_diary(request.POST)
    
    if v :
        context = {'mensaje': 'Gracias por suscribirte al diario de la Universidad.'}
   
    
    return HttpResponse(html_template.render(context, request))

def contact(request):
    
    
    return render(request, 'contact.html')

def postulante(request):
    
    
    return render(request, 'formulario.html')

def Send_diary(request):
    print("entro")
    subject = "Grcias estimado"
    mail = request.get('correo')
    message = "Gracias por suscribirte a nuestro diario."
    send_mail(subject, message, EMAIL_HOST_USER, [mail], fail_silently = False)
    return True