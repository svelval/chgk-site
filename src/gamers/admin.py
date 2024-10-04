from django.contrib import admin

from .models import Award, TVViewer, Connoisseur, Team


@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    model = Award
    list_display = ('name', 'description', )


@admin.register(TVViewer)
class TVViewerAdmin(admin.ModelAdmin):
    model = TVViewer
    list_display = ('user', 'first_name', 'last_name', 'about', 'get_awards', )


@admin.register(Connoisseur)
class ConnoisseurAdmin(admin.ModelAdmin):
    model = Connoisseur
    list_display = ('user', 'first_name', 'last_name', 'about', 'get_awards', 'first_game', 'won_games', 'total_games', )


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    model = Team
    list_display = ('get_gamers', 'is_active', 'first_game', 'won_games', 'total_games', )
