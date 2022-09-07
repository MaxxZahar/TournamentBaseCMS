from django.db import models


class TournamentModel(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название турнира')
    location = models.CharField(max_length=255, verbose_name='Место проведения')
    start_date = models.DateField(verbose_name='Дата начала турнира')
    finish_date = models.DateField(verbose_name='Дата конца турнира')

    class Meta:
        verbose_name = 'Турнир'
        verbose_name_plural = 'Турниры'
        ordering = ['-finish_date']

    def __str__(self):
        return self.name
