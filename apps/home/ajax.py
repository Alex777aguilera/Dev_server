from django.shortcuts import render

from django import template

from django.http import HttpResponse, HttpResponseRedirect
import json as simplejson, json
from rest_framework import serializers
from rest_framework.response import Response



from .models import *


def AJAXAdmisiones(request):
	if request.method == "GET" and request.is_ajax():
		print('entro al ajax')
		lista =[]
		if request.GET.get('id_carrera') is not None:
			id_carrera = request.GET.get('id_carrera')
			
			if Admisiones.objects.filter(carrera=int(id_carrera)).exists(): 
				data= Admisiones.objects.filter(carrera=int(id_carrera))
				lista = [{'descripcion_adm':data[0].descripcion_adm,'requisitos':data[0].requisitos,'fecha':str(data[0].fecha_expira)}]
				return HttpResponse(json.dumps(lista))
			else:
				lista= [{'Error':'No hay Admisiones para esta carrera'}]
			return HttpResponse(json.dumps(lista))
			
		else:
			lista= [{'Error':'Data None'}]
			return HttpResponse(json.dumps(lista))


def AJAXASolicitud(request):
	if request.method == "GET" and request.is_ajax():
		
		lista =[]
		if request.GET.get('id_solicitud') is not None:
			id_solicitud = request.GET.get('id_solicitud')
			
			if Solicitud.objects.filter(pk=int(id_solicitud)).exists(): 
				data= Solicitud.objects.filter(pk=int(id_solicitud))
				lista = [{'nombres':data[0].postulante.nombres+" "+data[0].postulante.apellidos,'correo':data[0].postulante.correo,'cel':data[0].postulante.cel, 'fecha':str(data[0].fecha_registro), 'carrera':data[0].admision.carrera.descripcion_carrera, 'des_ad':data[0].admision.descripcion_adm, 'requisitos':data[0].admision.requisitos}]
				# lista = [{'admision':data[0].postulante.nombres, 'fecha':str(data[0].fecha_registro)}]
				return HttpResponse(json.dumps(lista))
			else:
				lista= [{'Error':'No hay Solicitud para esta postulante'}]
			return HttpResponse(json.dumps(lista))
			
		else:
			lista= [{'Error':'Data None'}]
			return HttpResponse(json.dumps(lista))