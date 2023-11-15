from django.db import models


# Create your models here.

OPCIONES = [('Masculino','Masculino'), ('Femenino','Femenino'),('No Aplica','Prefiero no decirlo')]



class Director (models.Model):
 
    nombre = models.CharField(max_length=50)
    edad = models.PositiveIntegerField(default=1)
    genero = models.CharField(max_length=20,choices=OPCIONES)
    nacionalidad = models.CharField(max_length=50)
    premios = models.PositiveIntegerField(default=0)
    cantidad_peliculas = models.PositiveIntegerField(default=0)