from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os  


class Movie(models.Model):
    name = models.CharField(max_length=150)
    director = models.CharField(max_length=150)
    image = models.ImageField(upload_to='movies/covers')


@receiver(pre_delete, sender=Movie)
def delete_file_from_media(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)