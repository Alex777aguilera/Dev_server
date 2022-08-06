from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view, name="login"),
    # path('register/', register_user, name="register"),
    path("cerrar_secion/", cerrar_secion, name="logout"),
    path("administracion/", admin, name="administracion")
]
