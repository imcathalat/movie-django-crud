# Generated by Django 5.0.1 on 2024-02-06 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_uploads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(upload_to='movies/covers'),
        ),
    ]
