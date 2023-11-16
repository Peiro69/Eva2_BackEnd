from django.shortcuts import render
from appPelicula.forms import PeliculaForm
from appPelicula.models import Pelicula


# Create your views here.

def inicioAppPelicula(request):
    return render (request, 'appPelicula/inicioPelicula.html')


def formularioRegistroPelicula(request):
    form = PeliculaForm()
    if request.method == 'POST':
        form = PeliculaForm(request.POST)
        if form.is_valid():
            form.save()
        return inicioAppPelicula(request)
    data = {'form' : form}
    return render(request,'appPelicula/formularioPelicula.html',data)


def peliculaData(request):
    peliculas = Pelicula.objects.all()
    data = {'peliculas' : peliculas}
    return render(request, 'appPelicula/listadoPelicula.html', data)


def modificarPelicula(request, id):
    pelicula = Pelicula.objects.get(id = id)
    form = PeliculaForm(instance=pelicula)
    if request.method == 'POST':
        form = PeliculaForm(request.POST, instance=pelicula)
        if form.is_valid():
            form.save()
        return peliculaData(request)
    data = {'form' : form}
    return render(request, 'appPelicula/formularioPelicula.html',data)

