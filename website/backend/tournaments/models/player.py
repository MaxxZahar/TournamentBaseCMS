from django.db import models
from .tournament import TournamentModel


class PlayerModel(models.Model):
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='Дата рождения')
    federation = models.CharField(blank=True, null=True, max_length=255, verbose_name='Федерация')
    tournaments = models.ManyToManyField(TournamentModel)

    class Meta:
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
