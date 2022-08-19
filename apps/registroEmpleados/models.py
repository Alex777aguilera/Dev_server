from django.db import models
from django.contrib.auth.models import *
import datetime, time

# class Postulante(models.Model):
#   identidad = models.CharField(max_length = 50, null = False, blank = False)  
#   nombres = models.CharField(max_length = 100, null = False, blank = False)
#   apellidos = models.CharField(max_length = 100, null = False, blank = False)
#   cel = models.CharField(max_length = 50, null = False, blank = False)
#   correo = models.CharField( max_length = 50, null = False, blank = False)
#   archivo = models.BinaryField(null = False, blank = False)
#   fecha_registro = models.DateField(auto_now = True)
  
#   def __str__(self):
#         return f'{self.pk,self.nombres,self.apellidos, self.fecha_registro}'

# class Carrera(models.Model):
#     descripcion_carrera = models.CharField(max_length = 50, null = False, blank = False)
#     fecha_registro = models.DateField(auto_now = True)

#     def __str__(self):
#         return f'{self.pk,self.descripcion_carrera}'

# class Admisiones(models.Model):
#     descripcion_adm = models.CharField(max_length = 500, null = False, blank = False)
#     carrera = models.ForeignKey(Carrera,on_delete=models.CASCADE, null = False, blank = False)    
#     requisitos = models.CharField(max_length = 500, null = False, blank = False)
#     fecha_expira = models.DateField(auto_now = False, auto_now_add = False)
#     fecha_registro = models.DateField(auto_now = True)

#     def __str__(self):
#         return f'{self.pk,self.carrera.descripcion_carrera, self.fecha_expira}'

# class Solicitud(models.Model):
#     postulante = models.ForeignKey(Postulante, on_delete = models.CASCADE, null = False, blank = False)
#     admision = models.ForeignKey(Admisiones, on_delete = models.CASCADE, null = False, blank = False)
#     fecha_registro = models.DateField(auto_now = True)
#     estado_solicitud = models.BooleanField(default = False)
#     def __str__(self):
#         return f'{self.pk,self.admision.pk, self.admision.carrera.descripcion_carrera, self.estado_solicitud}'


# class Aprobacion(models.Model):
#     solicitd = models.ForeignKey(Solicitud,on_delete=models.CASCADE, null = False, blank = False)
#     usuario_registro = models.CharField(max_length = 50,  null = False, blank = False)
#     estado_aprobacion = models.BooleanField(default = False)
#     fecha_registro = models.DateField(auto_now = True)

#     def __str__(self):
#         return f'{self.pk,self.solicitd.postulante.nombres +""+self.solicitd.postulante.apellidos, self.estado_aprobacion, self.fecha_registro}'