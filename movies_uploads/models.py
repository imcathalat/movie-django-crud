from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=150)
    director = models.CharField(max_length=150)
    image = models.ImageField(upload_to='movies/covers')