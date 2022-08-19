from .models import *

def createElemenP(*args, **kwargs):
    obj = Postulante(**kwargs)
    obj.save()
    
    return obj.pk

def createElemenA(*args, **kwargs):
    obj = Admisiones(**kwargs)
    obj.save()
    
    return obj

def createElemenS(id_admision, id_p, *args):
    obj = Solicitud(admision = Admisiones.objects.get(pk = id_admision), postulante = Postulante.objects.get(pk = id_p))
    obj.save()
   
    return obj

def createElemenA(id_solicitud, user, estado, *args):
    obj = Aprobacion(solicitd = Solicitud.objects.get(pk = id_solicitud), usuario_registro = user, estado_aprobacion = estado)
    Solicitud.objects.filter(pk=id_solicitud).update(estado_solicitud=True)
    obj.save()
   
    return obj

