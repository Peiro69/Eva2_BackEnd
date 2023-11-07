from django.db import models

# Create your models here.

class Director (models.Model):
    nombreD = models.CharField(max_length=50)
    edadD = models.CharField(max_length=50)
    generoD = models.CharField(max_length=50)
    nacD = models.CharField(max_length=50)
    premiosD = models.CharField(max_length=50)
    cantPelis = models.CharField(max_length=50)
