from garpixcms.urls import *  # noqa
from django.urls import path, include

urlpatterns = [path('', include('tournaments.urls')),
               path('api/', include('api.urls'))] + urlpatterns  # noqa
