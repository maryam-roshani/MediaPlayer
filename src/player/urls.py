from media_player import views
from django.urls import path, include


urlpatterns = [
   path('admin/',views.media_player, name='media_player'),
]