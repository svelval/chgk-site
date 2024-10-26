import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse

from django.utils.translation import gettext_lazy as _

from gamers.models import Team


class Season(models.Model):
    class Meta:
        verbose_name = _('Season')
        verbose_name_plural = _('Seasons')
        ordering = ('year',)

    year = models.PositiveIntegerField(primary_key=True,
                                       validators=[MinValueValidator(2014),
                                                   MaxValueValidator(datetime.date.today().year)],
                                       verbose_name=_('year'))
    rules = models.TextField(verbose_name=_('rules'))
    connoisseurs_stat = models.PositiveIntegerField(default=0, verbose_name=_('connoisseurs stat'))
    tv_viewers_stat = models.PositiveIntegerField(default=0, verbose_name=_('TV viewers stat'))

    def __str__(self):
        return str(self.year)


class Group(models.Model):
    class Meta:
        verbose_name = _('Group')
        verbose_name_plural = _('Groups')
        unique_together = ('season', 'group_index', )
        ordering = ('group_index',)

    season = models.ForeignKey(to=Season, on_delete=models.CASCADE, verbose_name=_('season'))
    group_index = models.PositiveIntegerField(verbose_name=_('group index'))
    codename = models.CharField(verbose_name=_('codename'))
    name = models.CharField(verbose_name=_('name'))

    def __str__(self):
        return f'{self.name} {self.season}'


class Game(models.Model):
    class Meta:
        verbose_name = _('Game')
        verbose_name_plural = _('Games')
        unique_together = ('group', 'game_index', )
        ordering = ('game_index',)

    NAME_CHOICES = (
        ('first_game', _('First game')),
        ('second_game', _('Second game')),
        ('third_game', _('Third game')),
        ('fourth_game', _('Fourth game')),
        ('fifth_game', _('Fifth game')),
        ('final_game', _('Final game')),
        ('year_finale', _('Year finale')),
    )

    date = models.DateTimeField(primary_key=True, verbose_name=_('date'))
    group = models.ForeignKey(to=Group, on_delete=models.CASCADE, verbose_name=_('group'))
    game_index = models.PositiveIntegerField(default=1, verbose_name=_('game index'))
    name = models.CharField(choices=NAME_CHOICES, verbose_name=_('game name'))
    full_name = models.CharField(verbose_name=_('full name'))
    location = models.CharField(verbose_name=_('location'))
    best_player = models.ForeignKey(to='gamers.Connoisseur',
                                    on_delete=models.PROTECT,
                                    null=True,
                                    blank=True,
                                    related_name='best_players',
                                    verbose_name=_('best player'))
    prize_type = models.CharField(null=True, blank=True, verbose_name=_('prize type'))
    prize_winner = models.ForeignKey(to='gamers.Connoisseur',
                                     on_delete=models.PROTECT,
                                     null=True,
                                     blank=True,
                                     related_name='prize_winners',
                                     verbose_name=_('prize winner'))
    teams = models.ManyToManyField(to=Team, verbose_name=_('teams'))
    connoisseurs_score = models.PositiveIntegerField(default=0, verbose_name=_('connoisseurs score'))
    tv_viewers_score = models.PositiveIntegerField(default=0, verbose_name=_('tv viewers score'))

    def __str__(self):
        return str(self.full_name)
