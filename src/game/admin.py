from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Game, Group, Season


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
    list_display = ('group', 'group_index', 'get_teams', 'date', )
