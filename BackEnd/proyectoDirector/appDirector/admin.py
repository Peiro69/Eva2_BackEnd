from django.contrib import admin
from appDirector.models import Director

class DirectorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'edad', 'genero', 'fecha nacimiento', 'premios', 'cantidad de peliculas']

# Register your models here.

admin.site.register(Director)