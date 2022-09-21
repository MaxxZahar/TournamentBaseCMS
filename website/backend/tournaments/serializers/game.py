from rest_framework import serializers
from ..models import GameModel


class GameAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = GameModel
        fields = '__all__'
