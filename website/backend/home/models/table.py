from django.db import models


class TableModel(models.Model):
    table = models.FileField(verbose_name='Файл с таблицей')

    class Meta:
        verbose_name = 'Таблица'
        verbose_name_plural = 'Таблицы'

    def __str__(self):
        return f'File {self.table} uploaded'
