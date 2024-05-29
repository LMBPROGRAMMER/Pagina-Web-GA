from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def index (request):
    return render(request,'index.html',{
        'form':UserCreationForm
    })


def registro(request):
    return render(request,'registro.html')
@login_required
def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = "Credenciales inválidas. Inténtelo de nuevo."
            return render(request, 'index.html', {'error_message': error_message})
    else:
        return render(request, 'index.html')

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
    