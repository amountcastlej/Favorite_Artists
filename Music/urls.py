from fav_music import views
from django.urls import path, include

urlpatterns = [
    path('', views.index),
    path('artist/', include('fav_music.urls')),
]
