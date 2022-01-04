from django.urls import path
from .views import IndexView, GameplayView, check_answer, GoodPlayersView


urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('gameplay', GameplayView.as_view(), name='gameplay'),
    path('gameplay/check_answer', check_answer, name='check_answer'),
    path('good-player', GoodPlayersView.as_view(), name='score')
]