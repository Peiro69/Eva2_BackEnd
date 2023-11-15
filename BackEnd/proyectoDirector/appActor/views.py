from django.shortcuts import render
from appActor.forms import ActorForm
from appActor.models import Actor


# Create your views here.

def inicioAppActor(request):
    return render(request,'appActor/inicioActor.html')


def formularioRegistroDirector(request):
    form = ActorForm()
    if request.method == 'POST':
        form = ActorForm(request.POST)
        if form.is_valid():
            form.save()
        return inicioAppActor(request)
    data = {'form' : form}
    return render(request,'appActor/formularioActor.html',data)


def actoresData(request):
    actores = Actor.objects.all()
    data = {'actores': actores}
    return render(request,'appActor/listadoActor.html',data)


def modificarActor(request, id):
    actor = Actor.objects.get(id = id)
    form = ActorForm(instance=actor)
    if request.method == 'POST':
        form = ActorForm(request.POST, instance=actor)
        if form.is_valid():
            form.save()
        return actoresData(request)
    data = {'form' : form}
    return render(request, 'appActor/formularioActor.html', data)