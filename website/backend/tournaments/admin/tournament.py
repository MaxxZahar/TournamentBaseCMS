from django.contrib import admin
from ..models import TournamentModel


@admin.register(TournamentModel)
class TournamentModelAdmin(admin.ModelAdmin):
    pass
