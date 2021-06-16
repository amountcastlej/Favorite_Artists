from django.shortcuts import render, redirect
from .models import *

def index(request):
    context = {
        'artists': Artist.objects.all()
    }
    return render(request, 'artists.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):
    #Create an Artist!
    if request.method == "POST":
        Artist.objects.create(name=request.POST['name'], genre=request.POST['genre'])
    return redirect('/')

def delete(request, artist_id):
    #Delete one artist!
    to_delete = Artist.objects.get(id=artist_id)
    to_delete.delete()
    return redirect('/')

def edit(request, artist_id):
    one_artist = Artist.objects.get(id=artist_id)
    context = {
        'artist': one_artist
    }
    return render(request, 'edit.html', context)

def artist(request, artist_id):
    #Query for one artist with artist_id
    one_artist = Artist.objects.get(id=artist_id)
    context = {
        'artist': one_artist
    }
    return render(request, 'artist.html', context)

def update(request, artist_id):
    #update Artist
    if request.method == "POST":
        to_update = Artist.objects.get(id=artist_id)
    #update each field
        to_update.name = request.POST['name']
        to_update.genre = request.POST['genre']
        to_update.save()
    return redirect('/')

def create_album(request):
    #Create an Artist!
    if request.method == "POST":
        Album.objects.create(title=request.POST['title'], release_date=request.POST['release_date'], songs= request.POST['songs'], artist = request.POST['artist'])
    return redirect('/')

# Create your views here.
