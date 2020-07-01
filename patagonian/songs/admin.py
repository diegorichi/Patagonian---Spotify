from django.contrib import admin
from .models import Song, Artist


# Register your models here.
admin.site.register(Artist)
admin.site.register(Song)