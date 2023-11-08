from django.db import models

# Create your models here.

class Director (models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)
    premios = models.CharField(max_length=50)
    cantidad_peliculas = models.CharField(max_length=50)
