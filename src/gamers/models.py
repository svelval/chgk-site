from django.db import models

from django.utils.translation import gettext_lazy as _

from auth.models import User


class Award(models.Model):
    class Meta:
        verbose_name = _('Award')
        verbose_name_plural = _('Awards')

    codename = models.CharField(primary_key=True, verbose_name=_('codename'))
    name = models.CharField(verbose_name=_('name'))
    description = models.TextField(verbose_name=_('description'))
    pic = models.ImageField(upload_to='awards/', default='no_photo.jpg')

    def __str__(self):
        return str(self.codename)


class BasePlayer(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    first_name = models.CharField(verbose_name=_('first name'))
    last_name = models.CharField(verbose_name=_('last name'))
    about = models.TextField(verbose_name=_('description'))
    awards = models.ManyToManyField(to=Award, blank=True, verbose_name=_('awards'))

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_awards(self):
        return ', '.join(award for award in self.awards.all())


class TVViewer(BasePlayer):
    class Meta:
        verbose_name = _('TV Viewer')
        verbose_name_plural = _('TV Viewers')


class Connoisseur(BasePlayer):
    class Meta:
        verbose_name = _('Connoisseur')
        verbose_name_plural = _('Connoisseurs')

    first_game = models.ForeignKey(to='game.game',
                                   on_delete=models.PROTECT,
                                   null=True,
                                   blank=True,
                                   verbose_name=_('first game'))
    won_games = models.PositiveIntegerField(default=0, verbose_name=_('won games'))
    total_games = models.PositiveIntegerField(default=0, verbose_name=_('total games'))

    def finish_game(self, game):
        if self.total_games == 0:
            self.first_game = game.date
        self.total_games += 1
        self.save()

    def win(self, game):
        self.won_games += 1
        self.finish_game(game)

    def lose(self, game):
        self.finish_game(game)


class Team(models.Model):
    players = models.ManyToManyField(to=Connoisseur, related_name='teams', verbose_name=_('players'))
    captain = models.ForeignKey(to=Connoisseur,
                                on_delete=models.PROTECT,
                                related_name='captains',
                                verbose_name=_('captain'))
    is_active = models.BooleanField(default=True, verbose_name=_('is active'))
    first_game = models.ForeignKey(to='game.game',
                                   on_delete=models.PROTECT,
                                   null=True,
                                   blank=True,
                                   verbose_name=_('first game'))
    won_games = models.PositiveIntegerField(default=0, verbose_name=_('won games'))
    total_games = models.PositiveIntegerField(default=0, verbose_name=_('total games'))

    def __str__(self):
        return str(_('%(captain_name)s\'s team')) % {'captain_name': self.captain}

    def get_players(self):
        return ", ".join(str(player) for player in self.players.all())

    def archive(self):
        self.is_active = False

    def activate(self):
        self.is_active = True

    def win(self, game):
        self.won_games += 1
        self.total_games += 1
        self.save()
        for player in self.players.all():
            player.win(game)

    def lose(self, game):
        self.total_games += 1
        self.save()
        for player in self.players.all():
            player.lose(game)
