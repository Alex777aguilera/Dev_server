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

