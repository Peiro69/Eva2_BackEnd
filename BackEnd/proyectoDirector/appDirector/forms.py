from dataclasses import fields
from django import forms
from appDirector.models import Director


class FormDirector(forms.ModelForm):
    class Meta:
        model = Director
        fields = '__all__'
