from rest_framework import serializers
from ..models import PlayerModel


class PlayerSerializer(serializers.ModelSerializer):
    number_of_games = serializers.SerializerMethodField()
    number_of_wins = serializers.SerializerMethodField()

    class Meta:
        model = PlayerModel
        fields = '__all__'

    def get_number_of_games(self, obj):
        from ..models import GameModel
        games_1 = GameModel.objects.filter(player_1=obj)
        games_2 = GameModel.objects.filter(player_2=obj)
        return len(games_1) + len(games_2)

    def get_number_of_wins(self, obj):
        from ..models import GameModel
        games_1 = GameModel.objects.filter(player_1=obj).filter(result='+')
        games_2 = GameModel.objects.filter(player_2=obj).filter(result='-')
        return len(games_1) + len(games_2)
