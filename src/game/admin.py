from django.contrib import admin

from .models import Game, Group


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    model = Group
    list_display = ('name',)


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    model = Game
    list_display = ('year', 'group', 'group_index', 'get_teams', 'date', )
