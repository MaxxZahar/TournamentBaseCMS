from django.contrib import admin
from ..models import GameModel


@admin.register(GameModel)
class GameModelAdmin(admin.ModelAdmin):
    pass
