from .models import *
from rest_framework import serializers

class InputSerializerP(serializers.ModelSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
           
        return data

    class Meta:
        model = Postulante
        fields = (
            'nombres', 'apellidos', 'correo', 'cel', 'archivo', 'identidad'
        )

class InputSerializerA(serializers.ModelSerializer):
    def validate(self, attrs):
        print(attrs)
        data = super().validate(attrs)
        
        return data

    class Meta:
        model = Admisiones
        fields = (
            'descripcion_adm', 'carrera', 'requisitos', 'fecha_expira'
        )
