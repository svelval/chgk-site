from django.urls import path

from . import views

urlpatterns = [
    path('<int:season>/<str:group>/<int:group_index>', views.GameView.as_view(), name='game'),
]


