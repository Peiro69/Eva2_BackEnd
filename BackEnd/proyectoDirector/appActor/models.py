from django.db import models

# Create your models here.

class Actor (models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.PositiveIntegerField(default=1)
    genero = models.CharField(max_length=20)
    nacionalidad = models.CharField(max_length=50)
    premios = models.PositiveIntegerField(default=0)
    anio_debut = models.PositiveIntegerField(default=0)