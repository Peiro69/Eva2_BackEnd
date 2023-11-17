from django.db import models

# Create your models here.

OPCIONES = [('Masculino','Masculino'), ('Femenino','Femenino'),('No Aplica','Prefiero no decirlo')]

NACIONALIDAD = [('Estadounidense' , 'Estadounidense'), ('Británico','Británico'), ('Canadiense','Canadiense'),('Chileno','Chileno'), ('Peruano','Peruano'),('Otro','Otro')]



class Actor (models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.PositiveIntegerField(default='')
    genero = models.CharField(max_length=20, choices=OPCIONES)
    nacionalidad = models.CharField(max_length=50, choices=NACIONALIDAD)
    premios = models.PositiveIntegerField(default='')
    anio_debut = models.PositiveIntegerField(default='')

    def __str__(self):
        return f'{self.nombre}, {self.edad} años'