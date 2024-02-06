from django.forms import ModelForm
from django import forms
from .models import Movie

class UploadForm(ModelForm):
    name = forms.TextInput()
    director = forms.TextInput()
    image = forms.ImageField()

    class Meta:
        model = Movie
        fields = ['name', 'director', 'image']