from django.shortcuts import render
from appDirector.models import Director

# Create your views here.

def directorData(request):
    directores = Director.objects.all()
    data = {'directores':directores}
    return render(request,'appDirector/appDirector.html',data)