from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    #8000/artist/new
    path('new', views.new),
    #8000/artist/create
    path('create', views.create),
    #8000/'<int:artist_id>/delete
    path('<int:artist_id>/delete', views.delete),
    #8000/artist/<artist_id>/edit
    path('<int:artist_id>/edit', views.edit), 
    #8000/artist/<int:artist_id>
    path('<int:artist_id>', views.artist),
    path('<int:artist_id>/update', views.update),
    path('create_album', views.create_album),
]