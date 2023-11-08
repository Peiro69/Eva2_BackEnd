from django.shortcuts import render
from appDirector.models import Director
from . import forms

# Create your views here.

def directorData(request):
    directores = Director.objects.all()
    data = {'directores':directores}
    return render(request,'appDirector/appDirector.html',data)

def formularioRegistroDirector(request):
    form = forms.FormularioRegistroDirector()
    data = {'form' : form}
    return render(request,'appDirector/formularioDirector.html',data)

def inicioApp(request):
    return render(request,'appDirector/inicio.html')