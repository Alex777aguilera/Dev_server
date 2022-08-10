from ast import For
from django.shortcuts import render

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.core.mail import EmailMessage, send_mail
from config.settings import EMAIL_HOST_USER
import datetime, time
from .models import *
from .serializers import *
from .elements import *


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
    carreras = Carrera.objects.all()
    postulantes = Postulante.objects.all()
    
    ctx = {'carreras': carreras}
    if request.method == 'POST':
        id_admision = Admisiones.objects.get(carrera=int(request.POST.get('carrera')))
        
        serializer = InputSerializerP(data=request.POST)
        serializer.is_valid(raise_exception=True)
        id_p = createElemenP(
            **serializer.validated_data
        )
        createElemenS(
            int(id_admision.pk),
            int(id_p)
        )
        ctx = {'carreras': carreras, 'menssage':'Datos Guardados con exito!!'}
    return render(request, 'formulario.html', ctx)

def Send_diary(request):
    subject = "Gracias estimado"
    mail = request.get('correo')
    message = "Gracias por suscribirte a nuestro diario."
    send_mail(subject, message, EMAIL_HOST_USER, [mail], fail_silently = False)
    return True

def term_conditions(request):
    
    
    return render(request, 'term_conditions.html')

@login_required(login_url="/")
def admisiones(request):
    carreras = Carrera.objects.all()
    ctx = {'carreras': carreras}
    if request.method == 'POST':
        formatted_date = datetime.datetime.strptime(request.POST.get('fecha_expira'),'%m/%d/%Y')
        d = {'descripcion_adm':request.POST.get('descripcion_adm'), 'requisitos':request.POST.get('requisitos'), 'carrera': request.POST.get('carrera'), 'fecha_expira': formatted_date.date()}
        serializer = InputSerializerA(data=d)
        serializer.is_valid(raise_exception=True)
        createElemenA(
            **serializer.validated_data
        )
        ctx = {'carreras': carreras, 'menssage':'Datos Guardados con exito!!'}
    return render(request, 'admisiones.html', ctx)

@login_required(login_url="/")
def aprobaciones(request):
    solicitudes = Solicitud.objects.all().exclude(estado_solicitud=True)
    
    ctx = {'solicitudes':solicitudes}
    if request.method == 'POST':
        estado = False
        id_solicitud = Solicitud.objects.get(pk=int(request.POST.get('solicitud')))
        user = request.user
        if request.POST.get('v_aprobado') == 'on':
            estado = True
            createElemenA(id_solicitud.pk,user,estado)
        ctx = {'solicitudes':solicitudes, 'menssage': 'Datos Guardados con exito!!'}
    return render(request, 'aprobaciones.html',ctx)

def carreras(request):
    
    
    return render(request, 'carreras.html')

def medicina(request):
    
    
    return render(request, 'medicina.html')

def sistemas(request):
    
    
    return render(request, 'sistemas.html')

def electronica(request):
    
    
    return render(request, 'electronica.html')

def agronomia(request):
    
    
    return render(request, 'agronomia.html')

def derecho(request):
    
    
    return render(request, 'derecho.html')

def industrial(request):
    
    
    return render(request, 'industrial.html')

def psicologia(request):
    
    
    return render(request, 'psicologia.html')

def mecatronica(request):
    
    
    return render(request, 'mecatronica.html')