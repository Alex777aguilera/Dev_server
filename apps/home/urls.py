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
    path('carreras', carreras, name='carreras'),
    path('medicina', medicina, name='medicina'),

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]
