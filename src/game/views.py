from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.views.generic import DetailView

from .models import Game


class GameView(DetailView):
    template_name = 'game/game.html'
    model = Game

    def get_object(self, queryset=None):
        try:
            return self.model.objects.get(**self.kwargs)
        except ObjectDoesNotExist:
            raise Http404

    def get_context_data(self, **kwargs):
        context = super(GameView, self).get_context_data(**kwargs)
        context['game'] = self.object
        return context
