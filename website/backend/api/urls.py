from rest_framework import routers
from .viewsets import PlayersViewSet, TournamentsViewSet, GamesViewSet


api_router = routers.DefaultRouter()
api_router.register('players', PlayersViewSet)
api_router.register('tournaments', TournamentsViewSet)
api_router.register('games', GamesViewSet)

urlpatterns = []
urlpatterns += api_router.urls
