from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Award, TVViewer, Connoisseur, Team
from django.utils.translation import gettext_lazy as _


@admin.register(Award)
class AwardAdmin(TranslationAdmin):
    model = Award
    list_display = ('name', 'description', )


class BasePlayerAdmin(TranslationAdmin):
    list_display = ('user', 'first_name', 'last_name', 'about', 'get_awards',)

    def get_awards(self, obj):
        return ', '.join(award for award in obj.awards.all())

    get_awards.short_description = _('awards')


@admin.register(TVViewer)
class TVViewerAdmin(BasePlayerAdmin):
    model = TVViewer


@admin.register(Connoisseur)
class ConnoisseurAdmin(BasePlayerAdmin):
    model = Connoisseur

    def get_list_display(self, request):
        return super(ConnoisseurAdmin, self).list_display + ('first_game', 'won_games', 'total_games', )


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    model = Team
    list_display = ('get_players', 'is_active', 'first_game', 'won_games', 'total_games', )

    def get_players(self, obj):
        return ", ".join(str(player) for player in obj.players.all())

    get_players.short_description = _('players')
