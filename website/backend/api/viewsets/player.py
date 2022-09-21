from rest_framework import viewsets, mixins
from tournaments.models import PlayerModel
from tournaments.serializers import PlayerAPISerializer


class PlayersViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = PlayerModel.objects.all()
    serializer_class = PlayerAPISerializer


class PlayerDetailViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    queryset = PlayerModel.objects.all()
    serializer_class = PlayerAPISerializer
