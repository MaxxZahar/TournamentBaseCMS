from rest_framework import routers
from .viewsets import PlayersViewSet, TournamentsViewSet, GamesViewSet, PlayerDetailViewSet, TournamentDetailViewSet, \
    GameDetailViewSet


api_router = routers.DefaultRouter()
api_router.register('players', PlayersViewSet)
api_router.register('players', PlayerDetailViewSet)
api_router.register('tournaments', TournamentsViewSet)
api_router.register('tournaments', TournamentDetailViewSet)
api_router.register('games', GamesViewSet)
api_router.register('games', GameDetailViewSet)

urlpatterns = []
urlpatterns += api_router.urls
