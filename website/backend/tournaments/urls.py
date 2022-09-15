from django.urls import path
from .views import player, tournament


urlpatterns = [path('players/<int:player_id>', player),
               path('tournaments/<int:tournament_id>', tournament)]
