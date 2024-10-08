from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Game


class GameView(TemplateView):
    template_name = 'game/game.html'

    def get(self, request, *args, **kwargs):
        try:
            Game.objects.get(**kwargs)
        except ObjectDoesNotExist:
            raise Http404
        return super(GameView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(GameView, self).get_context_data(**kwargs)
        context['game'] = Game.objects.get(**kwargs)
        return context
