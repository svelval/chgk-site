import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from django.utils.translation import gettext_lazy as _

from gamers.models import Team


class Group(models.Model):
    class Meta:
        verbose_name = _('Group')
        verbose_name_plural = _('Groups')

    codename = models.CharField(primary_key=True, verbose_name=_('codename'))
    name = models.CharField(unique=True, verbose_name=_('name'))

    def __str__(self):
        return str(self.name)


class Game(models.Model):
    class Meta:
        verbose_name = _('Game')
        verbose_name_plural = _('Games')
        unique_together = ('year', 'group', 'group_index', )

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
    year = models.PositiveIntegerField(validators=[MinValueValidator(2014),
                                                   MaxValueValidator(datetime.date.today().year)],
                                       verbose_name=_('year'))
    group = models.ForeignKey(to=Group, on_delete=models.PROTECT, verbose_name=_('group'))
    group_index = models.PositiveIntegerField(default=1, verbose_name=_('game index'))
    name = models.CharField(choices=NAME_CHOICES, verbose_name=_('game name'))
    full_name = models.CharField(verbose_name=_('full name'))
    teams = models.ManyToManyField(to=Team, verbose_name=_('teams'))
    connoisseur_score = models.PositiveIntegerField(default=0, verbose_name=_('connoisseur score'))
    tv_viewers_score = models.PositiveIntegerField(default=0, verbose_name=_('tv viewers score'))

    def __str__(self):
        return str(self.full_name)

    def get_teams(self):
        return ', '.join(team for team in self.teams.all())
