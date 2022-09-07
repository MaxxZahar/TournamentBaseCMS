from django.contrib import admin
from ..models import PlayerModel


@admin.register(PlayerModel)
class PlayerModelAdmin(admin.ModelAdmin):
    pass
