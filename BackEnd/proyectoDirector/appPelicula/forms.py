from django import forms
from appPelicula.models import Pelicula 


class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = '__all__'