from django.db import models
from ..validators import validate_file_extension


class TableModel(models.Model):
    table = models.FileField(verbose_name='Файл с таблицей', validators=[validate_file_extension])

    class Meta:
        verbose_name = 'Таблица'
        verbose_name_plural = 'Таблицы'

    def __str__(self):
        return f'File {self.table} uploaded'
