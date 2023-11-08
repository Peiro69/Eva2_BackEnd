from dataclasses import fields
from django import forms
from appDirector.models import Director


class FormDirector(forms.ModelForm):
    class Meta:
        model = Director
        fields = '__all__'



class FormularioRegistroDirector(forms.Form):

    #OPCIONES = [{'masculino':'MASCULINO'}, {'femenino':'FEMENINO'},{'noAplica':'Prefiero no decirlo'}]


    nombre = forms.CharField(max_length=50)
    edad = forms.CharField(max_length=5)
    genero = forms.CharField(max_length=50)#(widget=forms.Select(choices=OPCIONES))
    nacionalidad = forms.CharField(max_length=50)
    numero_de_premios = forms.CharField(max_length=50)
    cantidad_de_Peliculas = forms.CharField(max_length=50)