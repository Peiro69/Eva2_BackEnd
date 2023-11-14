from django.shortcuts import render

# Create your views here.
def inicioAppActor(request):
    return render(request,'appActor/inicioActor.html')