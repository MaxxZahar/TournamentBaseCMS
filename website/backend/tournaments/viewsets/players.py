from rest_framework import viewsets, mixins
from ..models import PlayerModel
from ..serializers import PlayerAPISerializer


class PlayersViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = PlayerModel.objects.all()
    serializer_class = PlayerAPISerializer
