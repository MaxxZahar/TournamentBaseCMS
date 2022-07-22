from django.db import models
from .tournament import TournamentModel
from .player import PlayerModel


class GameModel(models.Model):
    player_1 = models.ForeignKey(PlayerModel, on_delete=models.CASCADE, related_name='player_1',
                                 verbose_name='Первый игрок')
    player_2 = models.ForeignKey(PlayerModel, on_delete=models.CASCADE, related_name='player_2',
                                 verbose_name='Второй игрок')
    tournament = models.ForeignKey(TournamentModel, on_delete=models.CASCADE, related_name='tournament',
                                 verbose_name='Турнир')
    leg = models.PositiveSmallIntegerField(verbose_name='Тур')
    result = models.CharField(max_length=1, verbose_name='Результат')
    handicap = models.CharField(blank=True, null=True, max_length=4, verbose_name='Фора')

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'

    def __str__(self):
        return f'{self.player_1}, {self.result}, {self.player_2}'
