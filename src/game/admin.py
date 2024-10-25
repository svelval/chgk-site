from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Game, Group, Season

from django.utils.translation import gettext_lazy as _


@admin.register(Season)
class SeasonAdmin(TranslationAdmin):
    model = Group
    list_display = ('year', 'connoisseurs_stat', 'tv_viewers_stat')


@admin.register(Group)
class GroupAdmin(TranslationAdmin):
    model = Group
    list_display = ('season', 'name', 'codename',)


@admin.register(Game)
class GameAdmin(TranslationAdmin):
    model = Game
    list_display = ('group', 'name', 'group_index', 'get_teams', 'date', )

    def get_teams(self, obj):
        return ', '.join(str(team) for team in obj.teams.all())

    get_teams.short_description = _('teams')
