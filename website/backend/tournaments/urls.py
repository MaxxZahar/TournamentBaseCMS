from django.urls import path
from .models import PlayerCardPage
from .views import player


urlpatterns = [path('players/<int:player_id>', player)]
