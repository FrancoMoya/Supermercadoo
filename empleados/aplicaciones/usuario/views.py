"""
#ELIMINAR
def registro (request):
    if request.method == 'GET':
        return render(request, 'usuario/registro.html',{
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('productos')
            except IntegrityError:
                return render(request, 'usuario/registro.html',{
                    'form': UserCreationForm,
                    'error': 'Usuario ya existe',
                })
        return render(request, 'usuario/registro.html',{
            'form': UserCreationForm,
            'error': 'Contraseña incorrecta',
            })

#ELIMINAR
def iniciar_sesion (request):
    if request.method == 'GET':
        return render(request, 'usuario/login.html',{
        'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'usuario/login.html',{
                'form': AuthenticationForm,
                'error': 'Usuario o Contraseña incorrecta'
            })
        else:
            login(request, user)
            return redirect('productos')
"""

from django.shortcuts import render, redirect
from .forms import UserForm, AuthForm
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import User
from django.contrib import messages
#from django.conf import settings
#from django.core.mail import send_mail

def home (request):
    return render(request, 'usuario/home.html')

def registro (request):
    form = UserForm()
    if request.method == 'GET':
        return render(request, 'usuario/registro.html',{
            'form': form
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(email=request.POST.get('email'),
                                                nombre=request.POST.get('nombre'),
                                                apellido=request.POST.get('apellido'),
                                                password=request.POST.get('password1')
                                                )
                print(request.POST) #PRINT
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'usuario/registro.html',{
                    'form': form,
                    'error': 'El usuario ingresado ya existe',
                })
        return render(request, 'usuario/registro.html',{
            'form': form,
            'error': 'Las contraseñas no coinciden',
            })

def iniciar_sesion (request):
    authF = AuthForm
    if request.method == 'GET':
        return render(request, 'usuario/login.html',{
        'form': authF
        })
    else:
        user = authenticate(request, email=request.POST['email'], password=request.POST['password'])
        if user is None:
            return render(request, 'usuario/login.html',{
                'form': authF,
                'error': 'Usuario o Contraseña incorrecta'
            })
        else:
            login(request, user)
            messages.success(request, "Iniciado correctamente")
            return redirect('home')

def cerrar_sesion (request):
    logout(request)
    return redirect('home')



