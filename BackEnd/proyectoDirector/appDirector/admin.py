from django.contrib import admin
from appDirector.models import Director

# Register your models here.

class DirectorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'edad', 'genero', 'nacionalidad', 'premios', 'cantidad_peliculas']

admin.site.register(Director, DirectorAdmin)