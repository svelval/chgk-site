from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Award, TVViewer, Connoisseur, Team


@admin.register(Award)
class AwardAdmin(TranslationAdmin):
    model = Award
    list_display = ('name', 'description', )


@admin.register(TVViewer)
class TVViewerAdmin(TranslationAdmin):
    model = TVViewer
    list_display = ('user', 'first_name', 'last_name', 'about', 'get_awards', )


@admin.register(Connoisseur)
class ConnoisseurAdmin(TranslationAdmin):
    model = Connoisseur
    list_display = ('user', 'first_name', 'last_name', 'about', 'get_awards', 'first_game', 'won_games', 'total_games', )


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    model = Team
    list_display = ('get_players', 'is_active', 'first_game', 'won_games', 'total_games', )
