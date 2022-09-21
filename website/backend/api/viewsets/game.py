from rest_framework import viewsets, mixins
from tournaments.models import GameModel
from tournaments.serializers import GameAPISerializer


class GamesViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = GameModel.objects.all()
    serializer_class = GameAPISerializer


class GameDetailViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    queryset = GameModel.objects.all()
    serializer_class = GameAPISerializer
