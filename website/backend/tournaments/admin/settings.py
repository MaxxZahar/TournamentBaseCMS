from django.contrib import admin
from ..models import SettingsModel


@admin.register(SettingsModel)
class SettingsModelAdmin(admin.ModelAdmin):
    pass
