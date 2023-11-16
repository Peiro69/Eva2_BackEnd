from django.contrib import admin
from appPelicula.models import Pelicula

# Register your models here.

class PeliculaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'minutos_duracion','genero','fecha_de_estreno','presupuesto','recaudacion','director','actor_protagonista']

admin.site.register(Pelicula, PeliculaAdmin)

