from django.urls import path, re_path
from apps.home.views import *
from apps.home.ajax import *

urlpatterns = [

    # The home page
    path('', index, name='home'),
    path('contact', contact, name='contact'),
    path('postulante', postulante, name='postulante'),
    path('term_conditions', term_conditions, name='term_conditions'),
    path('admisiones', admisiones, name='admisiones'),
    path('AJAXAdmisiones', AJAXAdmisiones, name='AJAXAdmisiones'),
    path('AJAXASolicitud', AJAXASolicitud, name='AJAXASolicitud'),
    ###### Carreras #######
    path('carreras', carreras, name='carreras'),
    path('medicina', medicina, name='medicina'),
    path('aprobaciones', aprobaciones, name='aprobaciones'),
    path('sistemas', sistemas, name='sistemas'),
    path('electronica', electronica, name='electronica'),
    path('derecho', derecho, name='derecho'),
    path('agronomia', agronomia, name='agronomia'),
    path('industrial', industrial, name='industrial'),
    path('psicologia', psicologia, name='psicologia'),
    path('mecatronica', mecatronica, name='mecatronica'),

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]
