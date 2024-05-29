from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages


def index (request):
    return render(request,'index.html',{
        'form':UserCreationForm
    })


def registro(request):
    return render(request,'registro.html')

def home(request):
    return render(request,'home.html')

def recibir_datos(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(email=email).exists():
            messages.error(request, 'El email ya está registrado')
        else:
            user = User.objects.create_user(username=email, first_name=nombre, email=email, password=password)
            user.save()
            messages.success(request, 'Usuario registrado con éxito')
            return redirect('index.html')  # Redirige a la página de login
    
    return render(request, 'registro.html')    
    