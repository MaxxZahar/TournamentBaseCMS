from django.db import models


class SettingsModel(models.Model):
    number_of_tournaments_in_pc =\
        models.PositiveIntegerField(blank=True, null=True, verbose_name='Количество турниров в карточке игрока')
    number_of_opponents_in_pc =\
        models.PositiveIntegerField(blank=True, null=True,
                                    verbose_name='Количество отображаемых оппонентов в карточке игрока')

    class Meta:
        verbose_name = 'Настройки'
        verbose_name_plural = 'Настройки'

    def __str__(self):
        return f'Настройки изменены'
