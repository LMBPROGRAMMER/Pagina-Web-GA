from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

def helloworld (request):
    return render(request,'index.html',{
        'form':UserCreationForm
    })


def registro(request):
    return render(request,'registro.html')
    