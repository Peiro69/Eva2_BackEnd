from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def display(request):
    return HttpResponse("<h1>hola mundo</h1>")

def renderTemplate(request):
    data = {"nombre":"peiro"}
    return render(request,'Ejercicio/Ejercicio.html',data)
