from django.forms import ModelForm, widgets
from django import forms
from .models import Movie

class UploadForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"
        widgets= {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'director': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'})
        }

class EditForm(forms.ModelForm):
    model = Movie

    renewal_name = forms.TextInput(attrs={'class': 'form-control'})
    renewal_director = forms.TextInput(attrs={'class': 'form-control'})
    renewal_image_cover = forms.FileInput(attrs={'class': 'form-control'})

