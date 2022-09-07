from django.contrib import admin
from ..models import TableModel
from ..utilities import handling_on_save


@admin.register(TableModel)
class TableModelAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        file = request.FILES['table'].readlines()
        handling_on_save(file)

        super().save_model(request, obj, form, change)
