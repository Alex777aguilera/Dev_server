from email import message
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,JsonResponse, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from .forms import LoginForm, SignUpForm
from apps.home.views import *

def login_view(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect("/administracion")
        else:
            return redirect("/")
    form = LoginForm(request.POST or None)
   
    msg = None

    if request.method == "POST":
        
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if request.user.is_superuser:
                   return redirect("/administracion")
                else:
                    return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "login.html", {"form": form, "msg": msg})


@login_required
def cerrar_secion(request):
    logout(request)
    return HttpResponseRedirect(reverse(index))

@login_required(login_url="/")
def admin(request):
    context = {'segment': 'index'}
   
    html_template = loader.get_template('admin.html')
    
    return HttpResponse(html_template.render(context, request))

