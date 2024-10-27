from django.urls import path

from . import views

urlpatterns = [
    path('<int:group__season>/<str:group__codename>/<int:game_index>', views.GameView.as_view(), name='game'),
]


