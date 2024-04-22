from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os  


class Movie(models.Model):
    name = models.CharField(max_length=150)
    director = models.CharField(max_length=150)
    image = models.ImageField(upload_to='movies/covers')

    def __str__(self):
        return self.name


class Review(models.Model):
    filme = models.ForeignKey('Movie', on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=60)
    content = models.TextField()
    bg_color = models.CharField(max_length=20)


@receiver(pre_delete, sender=Movie)
def delete_file_from_media(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)