from django.db import models
from .models import *

class Artist(models.Model):    
    name = models.CharField(max_length=60)
    genre = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Album(models.Model):
    title = models.CharField(max_length=60)
    release_date = models.DateTimeField()
    songs = models.CharField(max_length=60)
    artist = models.ForeignKey(Artist, related_name="album", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Create your models here.
