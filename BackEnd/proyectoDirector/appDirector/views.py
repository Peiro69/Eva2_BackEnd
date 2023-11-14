from contextlib import redirect_stderr
from django.shortcuts import render
from appDirector.models import Director
from . import forms
from appDirector.forms import FormDirector

# Create your views here.

def eliminarDirector(request, id):
    director = Director.objects.get(id = id)
    director.delete()
    directores = Director.objects.all()
    data = {'directores':directores}
    return render(request,'appDirector/appDirector.html', data)

def modificarDirector(request, id):
    director = Director.objects.get(id = id)
    form = FormDirector(instance=director)
    if request.method == 'POST':
        form = FormDirector(request.POST, instance=director)
        if form.is_valid():
            form.save()
        return inicioApp(request)
    data = {'form' : form}
    return render(request,'appDirector/formularioDirector.html',data)


def directorData(request):
    directores = Director.objects.all()
    data = {'directores':directores}
    return render(request,'appDirector/appDirector.html',data)

def formularioRegistroDirector(request):
    form = FormDirector()
    if request.method == 'POST':
        form = FormDirector(request.POST)
        if form.is_valid():
            form.save()
        return inicioApp(request)
    data = {'form' : form}
    return render(request,'appDirector/formularioDirector.html',data)

def inicioApp(request):
    return render(request,'appDirector/inicio.html')

def inicioProyecto(request):
    return render(request,'appDirector/inicioProyecto.html')