from django.contrib import admin

from .models import Game, Group, Season


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    model = Group
    list_display = ('year',)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    model = Group
    list_display = ('name', 'codename',)


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    model = Game
    list_display = ('season', 'group', 'group_index', 'get_teams', 'date', )
