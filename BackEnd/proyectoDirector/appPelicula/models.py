from django.db import models
from appActor.models import Actor
from appDirector.models import Director

# Create your models here.


OPCIONES_GENERO = [('Accion','Accion'),('Comedia','Comedia'),('Drama','Drama'),('Terror','Terror'),('Otros','Otros')]

class Pelicula (models.Model):

    titulo = models.CharField(max_length=30)
    minutos_duracion = models.PositiveIntegerField(default=0)
    genero = models.CharField(max_length=10,choices=OPCIONES_GENERO)
    fecha_de_estreno = models.DateField(null=False)
    presupuesto = models.PositiveIntegerField(default=0)
    recaudacion = models.PositiveIntegerField(default=0)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    actor_protagonista = models.ForeignKey(Actor,on_delete=models.CASCADE)