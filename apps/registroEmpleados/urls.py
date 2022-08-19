from django.urls import path
from apps.registroEmpleados.views import *


urlpatterns = [

    # The home page
    path('', index, name='home'),
    path('datos', datos, name='datos'),
    path('info', info, name='info'),
]
