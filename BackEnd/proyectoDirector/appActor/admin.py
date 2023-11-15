from django.contrib import admin
from appActor.models import Actor

# Register your models here.

class ActorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'edad', 'genero', 'nacionalidad', 'premios', 'anio_debut']

admin.site.register(Actor,ActorAdmin)