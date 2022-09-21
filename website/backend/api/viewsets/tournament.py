from rest_framework import viewsets, mixins
from tournaments.models import TournamentModel
from tournaments.serializers import TournamentAPISerializer


class TournamentsViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = TournamentModel.objects.all()
    serializer_class = TournamentAPISerializer


class TournamentDetailViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    queryset = TournamentModel.objects.all()
    serializer_class = TournamentAPISerializer
