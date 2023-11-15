from django import forms
from appActor.models import Actor  

class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = '__all__'