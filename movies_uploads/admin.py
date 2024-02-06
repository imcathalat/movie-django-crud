from django.contrib import admin
from .models import Movie


class MovieAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'image')

admin.site.register(Movie, MovieAdmin)