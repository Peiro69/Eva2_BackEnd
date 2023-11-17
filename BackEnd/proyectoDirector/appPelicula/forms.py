from django import forms
from appPelicula.models import Pelicula 


class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = '__all__' 
        widgets = {
           'fecha_de_estreno': forms.TextInput(attrs={'type': 'date', 'pattern': r'\d{2}/\d{2}/\d{4}'}),
        }