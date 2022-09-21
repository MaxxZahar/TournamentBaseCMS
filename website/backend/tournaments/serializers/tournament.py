from rest_framework import serializers
from ..models import TournamentModel


class TournamentSerializer(serializers.ModelSerializer):
    number_of_players = serializers.IntegerField()
    number_of_games = serializers.IntegerField()

    class Meta:
        model = TournamentModel
        fields = '__all__'

    def get_number_of_players(self, obj):
        return obj.tournament_players.all().count()

    def get_number_of_games(self, obj):
        return obj.tournament.all().count()


class TournamentAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = TournamentModel
        fields = '__all__'


class TournamentGameDetailAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = TournamentModel
        exclude = ('results',)
