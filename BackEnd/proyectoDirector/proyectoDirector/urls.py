"""
URL configuration for proyectoDirector project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appDirector import views as director
from appActor import views as actor
from appPelicula import views as pelicula

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', director.inicioProyecto),
    
    path('aplicacionDirector/', director.inicioApp),
    path('directores/', director.directorData),
    path('registroDirector/', director.formularioRegistroDirector),
    path('modificarDirector/<int:id>', director.modificarDirector),
    path('eliminarDirector/<int:id>', director.eliminarDirector),
    
    path('aplicacionActor/', actor.inicioAppActor),
    path('formularioActor/',actor.formularioRegistroDirector),
    path('listadoActores/', actor.actoresData),
    path('modificarActor/<int:id>', actor.modificarActor),
    path('eliminarActor/<int:id>', actor.eliminarActor),

    path('aplicacionPelicula/', pelicula.inicioAppPelicula),
    path('formularioPelicula/', pelicula.formularioRegistroPelicula),
    path('listadoPelicula/', pelicula.peliculaData ),
    path('modificarPelicula/<int:id>', pelicula.modificarPelicula),
    path('eliminarPelicula/<int:id>', pelicula.eliminarPelicula)


]
