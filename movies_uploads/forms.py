from django.forms import ModelForm, widgets
from django import forms
from .models import Movie, Review

class UploadForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"
        widgets= {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'director': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(UploadForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.TextInput(attrs={'class': 'form-control', 'id': 'ckeditor'}),
            'bg_color': forms.TextInput(attrs={'class': 'form-control'}),
        }


