from django.shortcuts import render

from django import template

from django.http import HttpResponse, HttpResponseRedirect
import json as simplejson, json
from rest_framework import serializers
from rest_framework.response import Response



from .models import *


class OutputSerializer_Admisiones(serializers.ModelSerializer):
    # puesto = serializers.CharField(source="puesto.descripcion_puesto")

    class Meta:
        model = Admisiones
        fields = '__all__'




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