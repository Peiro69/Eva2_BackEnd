from django.db import models


# Create your models here.

OPCIONES = [('Masculino','Masculino'), ('Femenino','Femenino'),('No Aplica','Prefiero no decirlo')]



class Director (models.Model):
 
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    genero = models.CharField(max_length=20,choices=OPCIONES)
    nacionalidad = models.CharField(max_length=50)
    premios = models.IntegerField()
    cantidad_peliculas = models.IntegerField()
