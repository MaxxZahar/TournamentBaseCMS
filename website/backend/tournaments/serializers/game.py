from rest_framework import serializers
from ..models import GameModel
from .player import PlayerGameDetailAPISerializer
from .tournament import TournamentGameDetailAPISerializer


class GameAPISerializer(serializers.ModelSerializer):
    player_1 = PlayerGameDetailAPISerializer(read_only=True)
    player_2 = PlayerGameDetailAPISerializer(read_only=True)
    tournament = TournamentGameDetailAPISerializer(read_only=True)

    class Meta:
        model = GameModel
        fields = '__all__'
