from django.urls import path
from .views import player, tournament


urlpatterns = [path('players/<int:player_id>', player, name='PlayerCard'),
               path('tournaments/<int:tournament_id>', tournament)]
