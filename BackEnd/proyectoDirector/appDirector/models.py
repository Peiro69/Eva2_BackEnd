from django.db import models


# Create your models here.

OPCIONES = [('Masculino','Masculino'), ('Femenino','Femenino'),('No Aplica','Prefiero no decirlo')]

NACIONALIDAD = [('Estadounidense' , 'Estadounidense'), ('Británico','Británico'), ('Canadiense','Canadiense'),('Chileno','Chileno'), ('Peruano','Peruano'),('Otro','Otro')]




class Director (models.Model):
 
    nombre = models.CharField(max_length=50)
    edad = models.PositiveIntegerField(default='')
    genero = models.CharField(max_length=20,choices=OPCIONES)
    nacionalidad = models.CharField(max_length=50,choices=NACIONALIDAD)
    premios = models.PositiveIntegerField(default='')
    cantidad_peliculas = models.PositiveIntegerField(default='')

    def __str__(self) -> str:
        return f'{self.nombre}, {self.edad} años'