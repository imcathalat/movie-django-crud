from django.contrib import admin
from .models import Movie, Review


class MovieAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'image')

admin.site.register(Movie, MovieAdmin)
admin.site.register(Review)