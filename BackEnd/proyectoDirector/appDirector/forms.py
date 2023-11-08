from django import forms

class FormularioRegistroDirector(forms.Form):
    nombre = forms.CharField(max_length=50)
    edad = forms.CharField(max_length=5)
    genero = forms.CharField(max_length=50)
    nacionalidad = forms.CharField(max_length=50)
    premios = forms.CharField(max_length=50)
    cantidad_de_Peliculas = forms.CharField(max_length=50)