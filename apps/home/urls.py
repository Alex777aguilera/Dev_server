from django.urls import path, re_path
from apps.home.views import *

urlpatterns = [

    # The home page
    path('', index, name='home'),
    path('contact', contact, name='contact'),
    path('postulante', postulante, name='postulante'),

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]
