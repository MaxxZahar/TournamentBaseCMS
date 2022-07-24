from django.contrib import admin
from ..models import TableModel


@admin.register(TableModel)
class TableModelAdmin(admin.ModelAdmin):
    pass
