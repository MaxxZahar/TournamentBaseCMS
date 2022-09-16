from django.db import models
import json


class TournamentModel(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название турнира')
    location = models.CharField(max_length=255, verbose_name='Место проведения')
    start_date = models.DateField(verbose_name='Дата начала турнира')
    finish_date = models.DateField(verbose_name='Дата конца турнира')
    results = models.JSONField(blank=True, null=True, verbose_name='Результаты турнира в формате JSON')

    class Meta:
        verbose_name = 'Турнир'
        verbose_name_plural = 'Турниры'
        ordering = ['-finish_date']

    def __str__(self):
        return self.name

    def get_players(self):
        results_dict = json.loads(self.results)
        return results_dict.get('players')

    def get_results(self):
        results_dict = json.loads(self.results)
        return results_dict.get('results')
