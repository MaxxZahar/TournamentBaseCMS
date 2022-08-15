from rest_framework import serializers
from ..models import TournamentModel, PlayerModel
from .player import PlayerSerializer


class TournamentSerializer(serializers.ModelSerializer):
    tournament_players = PlayerSerializer(many=True)
    number_of_players = serializers.SerializerMethodField()
    number_of_games = serializers.SerializerMethodField()

    class Meta:
        model = TournamentModel
        fields = '__all__'

    def get_number_of_players(self, obj):
        return obj.tournament_players.all().count()

    def get_number_of_games(self, obj):
        return obj.tournament.all().count()
